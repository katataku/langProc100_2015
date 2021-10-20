#! /usr/local/bin/python3

import sys,shelve,pyperclip
import re,os,shutil
import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - &(levelname)s - %(message)s')



word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = word.split()
print(list)
