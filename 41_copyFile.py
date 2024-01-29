import shutil

# copyfile() = copies contents of a FileExistsError
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

shutil.copyfile('test.txt', 'test2.txt')

shutil.copy('test.txt', 'test2.txt')

shutil.copy2('test.txt', 'test2.txt')