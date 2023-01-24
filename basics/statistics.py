from os import chdir
chdir('/mnt/c/Users/newta/OneDrive/Desktop')


def statistics(file1):
    with open(file1) as f1:
        lines_count = len(f1.readlines())
        f1.seek(0)
        words_count = len(f1.read().split())
        f1.seek(0)
        letters_count = len([x for x in f1.read()])

        stat = {
            'lines': lines_count,
            'words': words_count,
            'characters': letters_count
        }

        return stat


print(statistics('Alice.txt'))
