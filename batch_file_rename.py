#! /usr/bin/python
#coding=utf-8

#batch_file_rename.py
#Created:16 april 2019

'''
This will batch rename a group of files in a given directory,
once you pass the current an new extensions
'''

# just checking

__author__ = 'ahhxfeng'
__version__ = '1.0'

import os
import argparse

def batch_rename(work_dir, old_ext, new_ext):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current an new extensions
    '''
    #files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        #Get the file extension
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        #Start of the logic to check the file extension, if old_ext = file_ext
        if old_ext == file_ext:
            newfile = split_file[0] + new_ext
        else:
            os.rename(
                os.path.join(work_dir, filename)
                os.path.join(work_dir, newfile)
                #what's problem
            )
        
def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a wokring directory')
    parser.add_argument('work_dir', metavar= 'WORK_DIR', type=str, nargs=1, help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser

def main():
    '''
    This is be called if the script is directly invoked.
    '''
    #adding command line argument
    parser = get_parser()
    args = vars(parser.parse_args())

    #Set the variable work_dir with the first argument passed
    work_dir = args['work_dir'][0]
    old_dir = args['old_dir'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    else:
        pass
    new_dir = args['new_dir'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext
    else:
        pass

    batch_rename(work_dir, old_ext, new_ext)

if __name__ == "__main__":
    main()
    
