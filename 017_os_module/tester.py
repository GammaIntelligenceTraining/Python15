import os
import time

# CURRENT WORKING DIRECTORY
# print(os.getcwd())
# os.chdir('../')
# print(os.getcwd())
# print(os.listdir())
# os.mkdir(r'two')
# os.makedirs(r'new_folder\one\two\three')
# time.sleep(6)
# # os.rmdir(r'new_folder\one\two')
# os.remove(r'new_folder\one\two\three')
# os.removedirs(r'new_folder\one\two\three')

# os.rename('sample.mp3', 'new_folder/one/tester.mp3')

# print(os.stat('tester.py').st_size)

# info = os.walk(os.getcwd())
#
# for dirpath, dirnames, filenames in info:
#     print('*' * 20)
#     print('Current path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)

# print(os.environ.get('database_password'))  # change to your password

# print(os.environ.get('HOMEPATH') + r'\text.py')
# print(os.path.join('C:/home', "text.py"))

print(os.path.basename('/somedir/dir2/text.txt'))
print(os.path.dirname('/somedir/dir2/text.txt'))
print(os.path.split('/somedir/dir2/text.txt'))
print(os.path.splitext('/somedir/dir2/text.png'))

print(os.path.exists('new_folder1'))
print(os.path.isfile('new_folder'))
print(os.path.isdir('new_folder1'))
