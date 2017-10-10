import os, re
from shutil import copy
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

num_folders = 9
pth = os.getcwd()
pattern = 'dir_+\d'

def check_and_create_folder(pth):
    try:
        os.mkdir(pth)
        print('Created folder', pth)
    except FileExistsError:
        print('Already exists')
        
def create_several_folders(pth, num_folders):
    for i in range (1, num_folders+1):
        new_path = os.path.join(pth, 'dir_'+str(i))
        check_and_create_folder(new_path)
    print ('All folders created')    

def delete_several_folders(pth, pattern):
    for f in os.listdir(pth):
        if re.search(pattern, f):
            os.rmdir(os.path.join(pth, f))
            print ('Removed', f)
    print ('All matching folders removed')

#создаем 9 папок
create_several_folders(pth, num_folders) 

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def print_folders_in_cwd(pth):
    for file in os.listdir(pth):
        if os.path.isdir(file):
            print (file)

print ('Printing all folders in current working directory:')
print_folders_in_cwd(pth)

#удаляем 8 папок (завершение задачи-1)
delete_several_folders(pth, pattern)

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
