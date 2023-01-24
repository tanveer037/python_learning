from os import chdir
chdir('/mnt/c/Users/newta/OneDrive/Desktop')


def find_and_replace(file1,instance1,instance2):
    with open(file1, 'r+') as f1:
        content = f1.read()
        f1.seek(0)
        replaced_content = content.replace(instance1,instance2)
        f1.write(replaced_content)


find_and_replace('Colt.txt', 'Alice', 'Colt')