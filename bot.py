from datetime import datetime
import requests
import pywhatkit
import shutil
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


import sqlite3

import os

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


calendar_id = "yalmeida.rj@gmail.com"
# creds = Credentials.from_authorized_user_file('C:/Users/yalme/Desktop/ChatGPT/client_secret_833433804527-3fhghtg07tski5qmkdi0oaoj6hpqtrdi.apps.googleusercontent.com.json')
# api_key = "AIzaSyAXH3TYwuF0wszWhJioNpTAOlItZxeqIYU"
# service = build('calendar', 'v3', credentials=creds)
# calendar = service.calendars().get(calendarId='primary').execute()
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# class TimeManager:
#     def __init__(self):
#         self.creds = None
#         self.db = sqlite3.connect('events.db')
#         self.load_credentials()

#     def load_credentials(self):
#         """Loads the credentials from a token.json file if it exists, 
#         otherwise prompts the user to log in and grant access."""
#         if os.path.exists('token.json'):
#             self.creds = Credentials.from_authorized_user_file('token.json')
#         else:
#             pass
#             # Prompt user to log in and grant access
#             # Code to do so goes here

#     def addEvent(self, duration, description):
#         """Adds a new event to the Google Calendar with the specified duration and description."""
#         service = build('calendar', 'v3', credentials=self.creds)
#         event = {
#             'summary': description,
#             'start': {
#                 'dateTime': datetime.utcnow().isoformat() + 'Z',
#                 'timeZone': 'UTC',
#             },
#             'end': {
#                 'dateTime': (datetime.utcnow() + datetime.timedelta(hours=duration)).isoformat() + 'Z',
#                 'timeZone': 'UTC',
#             },
#         }
#         event = service.events().insert(calendarId=calendar_id, body=event).execute()
#         print(f'Event created: {event.get("htmlLink")}')


class LocalBot:
    """
    A class representing a LocalBot with a local_path and optional user_name and password.
    
    Attributes:
    local_path (str, optional): The local path where the bot will create or update the files. Default is 'C:/Users/yalme/Desktop/BotEntry'.
    user_name (str, optional): The user name to use when accessing the bot.
    password (str, optional): The password to use when accessing the bot.
    
    """    
    def __init__(self, local_path='C:/Users/yalme/Desktop', user_name=None, password=None):
        self.local_path = local_path
        self.user_name = user_name
        self.password = password
        self.sort_criteria = {
            ".txt": "text_files",
            ".pdf": "pdf_files",
            ".docx": "word_files",
            ".jpeg": "image_files",
            ".jpg": "image_files",
            ".png": "image_files",
            ".PNG": "image_files",
            ".gif": "image_files",
            ".svg": "image_files",
            ".mp3": "video_files",
            ".mp4": "video_files",
            ".MOV": "video_files",
            ".wav": "video_files",
            ".pptm": "power_point_files",
            ".py": "python_files",
            ".exe": "executable_files",
            ".zip": "zip_folders",
            ".json": "json_files",
            ".xlsx": "excel_files",
            ".xlsm": "excel_files",
            ".csv": "excel_files"
        }

    def update_directory_location(self, new_path:str=None) -> None:
        """
        Updates the location of the local directory.\n
        Prints new directory path.\n
        Args:
        new_path: The new location of the local directory. If not provided, it is set to Desktop.
        
        Returns:
        None     
        """
        self.local_path = new_path if new_path else 'C:/Users/yalme/Desktop'
        print(f"Bot has moved to a new path:\n{self.local_path}")

    def get_all_files(self):
        """
        This method prints a list of all the files in the local path.
        
        Returns:
        None
        """
        print([file for file in os.listdir(self.local_path)])

    def rename_file(self, old_file_name, new_file_name):
        """
        This method renames a file in the local path.
        
        Parameters:
        old_file_name (str): The current name of the file.
        new_file_name (str): The new name for the file.
        
        Returns:
        None
        """
        os.rename(os.path.join(self.local_path, old_file_name), 
                  os.path.join(self.local_path, new_file_name))

    def sort_files(self, folder_to_sort=None, sort_criteria=None):
        """
        Sorts files in the specified folder into different folders based on the file type.

        Parameters:
        folder_to_sort (str, optional): The path to the folder containing the files to sort. Defaults to None.
        sort_criteria (dict, optional): A dictionary that maps file extensions to the names of the folders to sort those file types into. Defaults to None.

        Returns:
        None
        """
        if sort_criteria is None:
            sort_criteria = self.sort_criteria
        if folder_to_sort is None:
            folder_to_sort = self.local_path

        for file_type, destination in sort_criteria.items():
            destination_path = os.path.join(folder_to_sort, destination)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            files = [f for f in os.listdir(folder_to_sort) if f.endswith(file_type)]
            for file in files:
                file_path = os.path.join(folder_to_sort, file)
                destination_file_path = os.path.join(destination_path, file)
                shutil.move(file_path, destination_file_path)

    def create_file(self, filename_and_type, context=None, path=None):
        """
        Create a new file with given filename + file_type and context. 
        
        If no context is provided, a default message including the current date and time will be used. 
        The file will be created in the provided path, or in the local_path attribute if no path is provided.
        
        Args:
        filename (str): The name of the file to be created, without the file extension.
        file_type (str): The file extension, including the dot (e.g. '.txt', '.pdf').
        context (str, optional): The content to be written in the file. Default is None.
        path (str, optional): The path where the file will be created. Default is None.
        
        Returns:
        None
        
        """
        filename, file_type = os.path.splitext(filename_and_type)
        if context is None:
            current_date = datetime.now().date()
            bot_msg = f"File created by localBot Assistant @ '{current_date}'"
            context = bot_msg
        
        if path is None:
            path = self.local_path
        
        my_file = path + "/" + filename + file_type
        with open(my_file, "w") as file:
            file.write(context)
        print(f"File '{my_file}' created successfully!")

    def update_file(filename, file_type, context, path=None):
        """
        Update an existing file with given filename, file_type, and context. 
        
        The file will be updated in the provided path, or in the local_path attribute if no path is provided.
        
        Args:
        filename (str): The name of the file to be updated, without the file extension.
        file_type (str): The file extension, including the dot (e.g. '.txt', '.pdf').
        context (str): The content to be appended to the file.
        path (str, optional):  The path where the file is located.
        """   
        if path is None:
            path = self.local_path
        my_file = path + '/' + filename + file_type
        try:
            with open(my_file, "a") as file:
                file.write(context)
            print(f"File '{my_file}' updated successfully!")
        except FileNotFoundError:
            print(f"File '{my_file}' not found.")

    def delete_file(self, file_name):
        """
        Deletes a file from the local path.

        Args:
        file_name: The name of the file to be deleted.

        Returns:
        None
        """
        try:
            os.remove(os.path.join(self.local_path, file_name))
            print(f"File {file_name} deleted successfully!")
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except:
            print(f"Unable to delete file {file_name}.")

    def read_file_content(self, file_name):
        try:
            with open(os.path.join(self.local_path, file_name), 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File {file_name} not found.")
            return None
        except:
            print(f"Unable to read file {file_name}.")
            return None

    def check_request_status(self, request_id):
        # Add code to check request status, e.g., making a GET request to a server
        pass
    
    def get_request_response(self, request_id):
        # Add code to retrieve the response of a request, e.g., by making a GET request to a server
        pass

    def send_request(url):
        """
        Sends a GET request to the specified url using the requests.get() method.
        If the request is successful (i.e., the server returns a status code of 200),
        the function returns the response body as text. If the request fails
        (i.e., the status code is not 200), the function returns an error message indicating the status code.
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Request failed with status code: {response.status_code}"        

    def send_whatsapp_message(self, phone_number, message, time=None):
        """
        Sends a WhatsApp message to the specified phone number.
        Args:
            phone_number (str): The phone number to send the message to.
            message (str): The message to send.
            time (str, optional): The time to send the message, in the format "HHMM". Defaults to None(sends instantly).

        Returns:
            None
        """        
        if time is None:
            pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=7, tab_close=True)
        else:
            hour = int(time[0:2])
            minute = int(time[2:4])
            pywhatkit.sendwhatmsg(phone_number, message, hour, minute, wait_time=7, tab_close=True)

    def send_mail(self, to_emails, html_content, from_email='yalmeida.rj@gmail.com', subject="An email scheduled by LocalBot!", time=126):
        message = Mail(
            from_email=from_email,
            to_emails=to_emails,
            subject=subject,
            html_content=html_content)
            # html_content='Hey Iury!\n How are you doing?\nChecking how it is And easy to do anywhere, even with Python')
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)

    def create_directory(self, file_name, local_path=None):
        """
        This function creates a directory at the specified local_path with the given file_name.
        
        local_path: The path where the directory will be created
        
        file_name: The name of the directory to be created
        
        Return: None
        """
        if local_path == None:
            local_path = self.local_path
        path = os.path.join(local_path, file_name)
        try:
            os.mkdir(path)
            print(f"Directory '{file_name}' created at '{local_path}'")
        except FileExistsError:
            print(f"Directory '{file_name}' already exists at '{local_path}'")
        except Exception as e:
            print(f"An error occurred while creating the directory: {e}")


    def get_all_methods_names(self, cls):
        """
        Returns the names of all methods in a class that don't start with two underscores.

        Parameters:
        cls (class): The class whose method names are to be returned.

        Returns:
        list: A list of strings, each representing the name of a method.
        
        Example:
        
        class MyClass:
            def method1(self):
                pass
            def method2(self):
                pass
            
        print(get_all_method_names(MyClass))
        # Output: ['method1', 'method2']
        """
        return [method for method in dir(cls) if callable(getattr(cls, method)) and not method.startswith("__")]
