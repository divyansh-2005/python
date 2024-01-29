# with open('test.txt') as file:
#     print(file.read())
# # with open auto closes files, but does not catch exception
    
# print(file.closed)

try:
    with open('text.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")