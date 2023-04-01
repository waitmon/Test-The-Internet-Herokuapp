import random


def generated_file():
    path = rf'/Users/anton/PycharmProjects/Test-The-Internet-Herokuapp/test.{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello Test{random.randint(0, 999)}')
    file.close()
    return file.name, path
