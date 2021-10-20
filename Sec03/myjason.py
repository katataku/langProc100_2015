#! /usr/local/bin/python3

import sys,shelve,pyperclip
import re,os,shutil
import random
import logging,json

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - &(levelname)s - %(message)s')


reg2 = re.compile(r'^={2}([^=]*)={2}$')
reg3 = re.compile(r'^={3}([^=]*)={3}$')
reg_media = re.compile(r'ファイル:([^|]*)|')
reg_basic = re.compile(r'基礎情報(.*?)\n(.*)\n\}\}',re.DOTALL) 

jd = json.JSONDecoder()
f = open("jawiki-country.json", 'r')
for line in f:
    json_data = json.loads(line)
    if json_data['title'] == 'イギリス' :
        mo_basic = reg_basic.search(json_data['text'])
        if mo_basic != None:
            print(mo_basic.group(2))

'''
    lines = json_data['text'].split('\n')
    if json_data['title'] == 'イギリス' :
        for l in lines :
            if '基礎情報' in l:
                print(l)

            mo_media = reg_media.search(l)
            if mo_media.group() != '':
                print(mo_media.group())
            mo2 = reg2.search(l)
            mo3 = reg3.search(l)
            if mo2 != None :
                print('2: ' +mo2.group(1))
            elif mo3 != None:
                print('3: ' +mo3.group(1))

    for l in lines:
        if 'Category' in l:
            cat = l[11:-2]
            logging.debug('title: {} ,cat: {}'.format(json_data['title'],cat))
'''

    


      
