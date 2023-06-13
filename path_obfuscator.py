#!/bin/python3
import os
import platform
import sys
import random

has_drive = 0

# check running operating system
if platform.system() == 'Windows':
    local_os = 0
elif platform.system() == 'Linux':
    local_os = 1

# obfuscate string function
def obfuscate_string(input_string):
    obfuscated_string = ''
    previous_char = ''
    
    for char in input_string:
        if char == previous_char == '*':
            continue  # Skip consecutive '*' characters in input string
        if random.randint(1, 4) == 1:
            obfuscated_string += char
            previous_char = char
        elif random.randint(0, 1) == 0:
            if previous_char == '*' and char == '*':
                continue
            obfuscated_string += '*'
            previous_char = '*'
        else:
            obfuscated_string += '?'
            previous_char = '?'
        previous_char = char
    return obfuscated_string

# print the obfuscated path
def print_obfuscated_path():
    if has_drive == 0:
        print('Obfuscated path: ' + '/' + '/'.join(path_parts))
    elif has_drive == 1:
        print('Obfuscated path: ' + '\\'.join(path_parts))

#re-add drive letter if needed (C: is assumed as default)
def drivecheck():
    if has_drive == 1:
        path_parts.insert(0, 'C:')

check = input('Are you checking local path or remote path? (l/r): ').lower()
# remote path check
if check == 'r':
    path = input('Enter a path: ')  
    # split path variable into parts delimited by a \ or /
    path_parts = path.split('\\') if '\\' in path else path.split('/')
    if ':' in path_parts[0]:
        has_drive = 1
        path_parts.pop(0)
    else:
        has_drive = 0
    # obfuscate strings in path_parts list with ?, *, or actual letter
    for i in range(len(path_parts)):
        path_parts[i] = obfuscate_string(path_parts[i])
    drivecheck()
    print_obfuscated_path()
# local path check
elif check == 'l':
    path = input('Enter a path: ')
    # split path variable into parts delimited by a \ or /
    path_parts = path.split('\\') if '\\' in path else path.split('/')
    # search local disk for path and recursivly print all files and folders
    # find unique strings of each UNC path and print them
    current_path = ''
    final_filename = []
    for i in range(len(path_parts)):

        # recreating next path to listdir
        current_path = current_path + '/' + path_parts[i]
        print('Current path: ' + current_path)
        if os.path.exists(current_path):
            files_found = os.listdir(current_path)
            print('Files found: ' + str(files_found))
            # Time for a stupid nested ifs and fors :D Hopefully this works
            for j in range(len(files_found)):

                if files_found[j] not in path_parts[i]:
                    new_file_list = []
                    matchy = ''
                    print('Found a unique string: ' + files_found[j])

                    for k in range(len(path_parts[i])):
                        # randomize everything, all the time

                        for l in range(len(files_found[j]), len(path_parts[i])):
                            files_found[j] = files_found[j] + '*'

                        if path_parts[i][k] != files_found[j][k]:
                            if random.randint(0,1) == 1:
                                new_file_list.append(path_parts[i][k])
                                matchy = files_found[j][k]
                            elif random.randint(0, 1) == 0:
                                if random.randint(0, 1) == 1:
                                    if matchy == '*':
                                        continue
                                    else:
                                        new_file_list.append('*')
                                        matchy = '*'
                            elif random.randint(0, 1) == 0:
                                new_file_list.append('?')
                                matchy = '?'
                        else:
                            if random.randint(0, 1) == 1:
                                if matchy == '*':
                                    continue
                                else:
                                    new_file_list.append('*')
                                    matchy = '*'
                            elif random.randint(0, 1) == 0:
                                new_file_list.append('?')
                                matchy = '?'
                    new_file_list.append('/')
        else: 
            print('Path does not exist')
            sys.exit()
    drivecheck()
    print_obfuscated_path()
