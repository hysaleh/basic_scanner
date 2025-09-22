#!/usr/bin/env python3
import sys, os, shutil, re
from pathlib import Path


skip=["node_modules","public",".next"]
high=[".env",".bak",".swp","old",".backup"]

def first_line(path):
    for entry in os.scandir(path): 
        if entry.is_file() and "env" in entry.name and ".next" not in entry.name and "node_modules" not in entry.name:
            with open(entry,'r') as r:
                print(r.readline())

        elif entry.is_dir():
            first_line(entry)

print(first_line('/Users/heba/Jobpher-'))


#making sure files types such as .env, .bak, and .swp don't live in prod.
#if they do
#1) check file perms
#2) lightweight inspection....scan for patterns that indicate keys or tokens

def secrets_detection():
    for match in re.match("")


def report():
    print()





# '''
# # To get a list of all the files and folders in a particular
# # directory in the filesystem----> os.scandir. os.listdir is outdated

# files=os.scandir('.')
# print(f'Here is the iterator for our files: \n {files}')
# print("*********")
# looped=[ file.name for file in files]
# print(f'Here is each entrys name after we looped through the iterator {looped}')
# print("*********")


# #Remember that iterating over a string gives you one character at a time
# #simple utility to return contents of a text file

# def usage():
#     print(("Usage: ./scanner.py <subcommand>"),file=sys.stderr

#     )
# file_path=sys.argv[1]

# trgt_exts=[".txt",".pub",".bak"]
# excl_exts=[".md"]


# print(f'printing all contents of the file given: \n')
# def file_info(file_path):
#     with open(file_path,'r') as f:
#         contents=f.read()
#         print(contents)

# for directory in os.scandir():
#     print(directory,":::::DirEntry")
# for subdir in os.listdir(directory):
#     print(subdir,"subfile?")


# # .read() returns one big string with the whole file in it
# # When you later do for line in contents....you’re actually iterating over THAT string


# # if file_path in sys.argv:
# #     (file_info(file_path))
#     # # print(file_info(file_path) <--- returns None
#     # print(os.path.exists(file_path))



# # Ensure that you are iterating over the iterator returned by os.scandir(), 
# # and not attempting to iterate over individual os.DirEntry objects.



# #an iterator is simply any object you can iterate over






