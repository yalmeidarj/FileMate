# LocalBot Class - Introduction

LocalBot is a class representing a bot. It provides methods to update directory location, get a list of all the files, rename a file, sort files, create a new file, send WhatsApp message, send emails, and create new directorys in the local path.

## Class Attributes

### local_path (str, optional):

The local path where the bot will create or update the files. Default is {desktop_path}.

### user_name (str, optional):

The user name to use when accessing the bot.

### password (str, optional):

The password to use when accessing the bot.

## Class Methods

### update_directory_location

Updates the location of the local directory.

#### Args:

### new_path (str):

The new location of the local directory. If not provided, it is set to Desktop.
Returns:
None

Example:

```

bot = LocalBot()

bot.update_directory_location('C:/Users/newuser/Desktop')

```

##

### get_all_files

This method returns a list of all the files in the local path.

#### Returns:

None

Example:

```
Copy code
bot = LocalBot()
bot.get_all_files()
```

##

### rename_file

This method renames a file in the local path.

#### Args:

### old_file_name (str):

The current name of the file.

### new_file_name (str):

The new name for the file.
Returns:
None

Example:

```

bot = LocalBot()
bot.rename_file('old_file.txt', 'new_file.txt')
```

##

### sort_files

Sorts files in the specified folder into different folders based on the file type.

#### Args:

### folder_to_sort (str, optional):

The path to the folder containing the files to sort. Defaults to None.

### sort_criteria (dict, optional):

A dictionary that maps file extensions to the names of the folders to sort those file types into. Defaults to None.
Returns:
None

Example:

```

bot = LocalBot()

bot.sort_files(folder_to_sort='C:/Users/newuser/Desktop/unsorted_files', sort_criteria={
    ".txt": "text_files",
    ".pdf": "pdf_files"

})

```

##

### create_file

Create a new file with given filename, file_type and context.

#### Args:

### filename (str):

The name of the new file to be created.

### file_type (str):

The type of the file to be created.

### context (str, optional):

The content of the file. If not provided, a default message including the current date and time will be used.

### path (str, optional):

The location where the file will be created. If not provided, the file will be created in the local path.
Returns:
None

Example:

```
bot = LocalBot()

bot.create_file('new_file.txt', '.txt', 'Hello, World!', 'C:/Users/newuser')

```

##

### get_all_methods_names:

Returns the names of all methods in a class that don't start with two underscores.

#### Parameters:

cls (class): The class whose method names are to be returned.

#### Returns:

list: A list of strings, each representing the name of a method.

Example:

```
class MyClass:
  def method1(self):
    pass
  def method2(self):
    pass

  print(get_all_methods_names(MyClass))
  # Output: ['method1', 'method2']
```
