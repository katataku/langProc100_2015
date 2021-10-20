#! /usr/local/bin/python3

import sys,shelve,pyperclip
import re,os,shutil
import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - &(levelname)s - %(message)s')



word1 = 'パトカー'
word2 = 'タクシー'
word = ''
for i in range(4):
    word = word + word1[i]
    word = word + word2[i]
print(word)


