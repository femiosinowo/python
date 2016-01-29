#!/usr/bin/env python

import subprocess


#function to print my filesystem
def myFileSystem():
        print "this is going to print the filesystem:\n"
        subprocess.call('df -h' , shell=True)
        print "/n"
        subprocess.
#print time
def myTime():
        subprocess.call('date', shell=True)

def main():
        myFileSystem()
        myTime()


main()