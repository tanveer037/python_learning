from os import chdir
chdir('/mnt/c/Users/newta/OneDrive/Desktop')

# f = open('New Text Document.txt')
# print(f.read())
# f.close()

with open('New Text Document.txt') as f:
    print(f.read())
