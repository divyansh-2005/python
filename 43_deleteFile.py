import os
import shutil

path = "test.txt"
folderPath = 'folder'

# try:
    # os.remove(path) #delete a file
# except FileNotFoundError:
#     print("That file was not found")

try:
    # os.rmdir(folderPath)      #delete an empty directory
    shutil.rmtree(folderPath)   #delete a directory containg files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You can't delete using that function")
else:
    print(folderPath+" was deleted")
