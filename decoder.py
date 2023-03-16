import os
import subprocess
import time

files = open('files.txt', 'r+')

#for line in files:
ok = open('ok.txt', 'r+')
#    ok.write(line.replace('у�', 'п').replace('Г�', 'о').replace('ш�', 'щ'))


i = 0

while i <= 20:

    path = '/Users/aroslavgorodilov/Desktop/devops_courses/'

    ok_line = ok.readlines()
    file_line = files.readlines()

    old_name = os.path.join(path, file_line[i]).replace('\n', '')
    new_name = os.path.join(path, ok_line[i]).replace('\n', '')

    print(f'Before: {ok_line[i]}')
    os.rename(old_name, new_name)
    print(f'After: {ok_line[i]}')
    i += 1
    time.sleep(1.5)
