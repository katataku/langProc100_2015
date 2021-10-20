#! /usr/local/bin/python3

import sys,shelve,pyperclip
import re,os,shutil
import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - &(levelname)s - %(message)s')



words = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."


word = words.split()
shuffled = []
for l in word:
    if len(l) > 3 :
        mid_list = list(l[1:-1])
        random.shuffle(mid_list)
        l = l[0] + "".join(mid_list)+l[-1]
    shuffled.append(l)
    logging.debug('l={}'.format(l))
print(" ".join(shuffled))
      
