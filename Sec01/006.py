#! /usr/local/bin/python3

import sys,shelve,pyperclip
import re,os,shutil
import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - &(levelname)s - %(message)s')


def l_2gram(word,dic):
    for i in range(len(word)-1):
        out = []
        out.append(word[i])
        out.append(word[i+1])
        dic.setdefault(i,out)
    
def w_2gram(word,dic):
    list = word.split()
    for i in range(len(list)-1):
        out = []
        out.append(list[i])
        out.append(list[i+1])
        dic.setdefault(i,out)
    
        

word1 = "kparaparaparadise"
word2 = "paragraph"


dic1 = {}
dic2 ={}
l_2gram(word1,dic1)
l_2gram(word2,dic2)


val1 = list(dic1.values())
val2 = list(dic2.values())

intercect_list = []
for v1 in val1:
    intercect_list +=filter(lambda v2:v2 == v1,val2)

print('intersect_list = ',intercect_list)





