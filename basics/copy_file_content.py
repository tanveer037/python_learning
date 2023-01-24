from os import chdir
chdir('/mnt/c/Users/newta/OneDrive/Desktop')


def copy(file1, file2):
    with open(file1) as f1:
        content1 = f1.read()
        with open(file2, 'w') as f2:
            f2.write(content1)


copy('Alice.txt', 'Colt.txt')
