import os, re, sys
from shutil import copy

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

num_folders = 9
cpth = os.getcwd()
pattern = 'dir_+\d'

def check_and_create_folder(pth=cpth):
    try:
        os.mkdir(pth)
        print('Created folder', pth)
    except FileExistsError:
        print('Already exists')


def create_several_folders(pth=cpth, num=num_folders):
    for i in range (1, num+1):
        new_path = os.path.join(pth, 'dir_'+str(i))
        check_and_create_folder(new_path)
    print ('All folders created')


def delete_several_folders(pth=cpth, pattern=pattern):
    for f in os.listdir(pth):
        if re.search(pattern, f):
            os.rmdir(os.path.join(pth, f))
            print ('Removed', f)
    print ('All matching folders removed')


def remove_folder(dir_name):
    try:
        os.rmdir(os.path.join(os.getcwd(), dir_name))
        print ("Успешно удалено")
    except FileNotFoundError as e:
        print ("No folder with this name: ", e)

#создаем 9 папок
# create_several_folders(cpth, num_folders)
#удаляем 8 папок
# delete_several_folders(cpth, pattern)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def print_folders_in_cwd(dir_name):
    for file in os.listdir(dir_name):
        if os.path.isdir(file):
            print (file)

# print ('Printing all folders in current working directory:')
# print_folders_in_cwd(cpth)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def make_self_copy():
    dir_path = os.getcwd()
    input = os.path.abspath(__file__)
    filename, extension = os.path.splitext(__file__)
    output = os.path.join(dir_path, filename+'_copy'+extension)
    copy(input, output)
    print ('Self copy done')

make_self_copy()

def goto(dir_name):
    pth = os.getcwd()
    new_path = os.path.join(pth, dir_name)
    os.chdir(new_path)
    print ("Now we in: ", os.getcwd())
    print ("Folders: ")
    print_folders_in_cwd(new_path)


def create_folder(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
