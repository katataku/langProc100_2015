#! /usr/local/bin/python3

import sys,shelve,pyperclip
import re,os,shutil
import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - &(levelname)s - %(message)s')


def w_2gram(word,dic):
    for i in range(len(word)-1):
        out = []
        out.append(word[i])
        out.append(word[i+1])
        dic.setdefault(i,out)
    
def l_2gram(word,dic):
    list = word.split()
    for i in range(len(list)-1):
        out = []
        out.append(list[i])
        out.append(list[i+1])
        dic.setdefault(i,out)
    
        

word = "I am an NLPer"
dic1 = {}
dic2 ={}
w_2gram(word,dic1)
l_2gram(word,dic2)



print("er" in dic1.values())


