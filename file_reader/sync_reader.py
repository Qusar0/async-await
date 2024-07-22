import datetime
import time
import os

def read_file(filename):
    with open(filename, mode='rb') as f:
        print("\n######start######", filename, sep="\n")
        while True:
            time.sleep(0.001)
            data = f.read(1024)
            if not data:
                print(filename, "#######done######", sep="\n")
                break

def generator_helper(address, names):
    for name in names:
        if name.endswith(".bin"):
            yield os.path.join(address, name)

def generator(path):
    for address, dirs, files in os.walk(path):
        yield from generator_helper(address, files)


def main():
    # /home/user/sia/tmp/
    path = input("Enter path to binary files: ")
    begin = datetime.datetime.now()
    files = [item for item in generator(path)]

    if len(files) == 0:
        raise ValueError("No binary files in {}".format(path))

    for f in files:
        read_file(f)

    print(datetime.datetime.now() - begin)

main()
