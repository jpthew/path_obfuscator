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
        print('Obfuscated path: ' + '/' + '/'.join(l_obfuscated))
    elif has_drive == 1:
        print('Obfuscated path: ' + '\\'.join(l_obfuscated))

#re-add drive letter if needed (C: is assumed as default)
def drivecheck():
    if has_drive == 1:
        l_obfuscated.insert(0, 'C:')

# compare list and obfuscate on the 'against' parameter
def compare_obfuscate(list, against):
    new_list = []
    new_path = []
    # word formatting: extending word, create wordlist, removing word if complete match (should always happen)
    for word in list:
        if word == against:
            continue
        if len(word) < len(against):
                word_delta = len(against) - len(word)
                word = word + ('?' * word_delta)
        for i in range(len(against)):
            if word[i] == against[i]:
                #print(word)
                new_list.append(word)
                break
            

    # masking on the 'against' parameter from the wordlist
    for i in range(len(against)):
        var = 0
        for word in new_list:
            if word[i] == against[i]:
                var = 1
        if var == 1:
            new_path.append('?')
        elif var == 0:
            new_path.append(against[i])
    
    new_path_str =  "".join(new_path)
    new_path_str = new_path_str.replace('??', '*')
    return new_path_str

check = input('Are you checking local path or remote path? (l/r): ').lower()
# remote path check
if check == 'r':
    path = input('Enter a path: ')  
    # split path variable into parts delimited by a \ or /
    path_part = path.split('\\') if '\\' in path else path.split('/')
    if ':' in path_part[0]:
        has_drive = 1
        path_part.pop(0)
    else:
        has_drive = 0
    # obfuscate strings in path_parts list with ?, *, or actual letter
    for p_iterator in range(len(path_part)):
        path_part[p_iterator] = obfuscate_string(path_part[p_iterator])
        l_obfuscated = path_part
    drivecheck()
    print_obfuscated_path()


# local path check
elif check == 'l':
    path = input('Enter a path: ')
    path_part = path.split('\\') if '\\' in path else path.split('/')
    if ':' in path_part[0]:
        has_drive = 1
        path_part.pop(0)
    else:
        has_drive = 0
    for i in range(len(path_part)):
        if path_part[i] == '':
            path_part.pop(i)
            break
    current_path = ''
    final_filename = []
    for p_iterator in range(len(path_part)):

        # recreating next path to listdir
        current_path = '/'
        if os.path.exists(path):
            l_obfuscated = []
            #print('Files found: ' + str(files_found))
            # Time for a stupid nested ifs and fors :D Hopefully this works
            for i in range(len(path_part)):
                files_found = os.listdir(current_path)
                check = path_part[i]
                obfuscated_string = compare_obfuscate(files_found, check)
                l_obfuscated.append(obfuscated_string)
                current_path += path_part[i] + '/'
            break
        else: 
            print('Path does not exist')
            sys.exit()
    drivecheck()
    print_obfuscated_path()