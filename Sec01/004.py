#! /usr/local/bin/python3

import sys,shelve,pyperclip
import re,os,shutil
import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - &(levelname)s - %(message)s')



word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

tar = [1,5,6,7,8,9,15,16,19]
dic = {}
list = word.split()

for i in range(20):
    if i+1 in tar: 
        dic.setdefault(i,list[i][0])
    else:
        dic.setdefault(i,list[i][:2])

print(dic)        



