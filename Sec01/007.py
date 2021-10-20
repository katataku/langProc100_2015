#! /usr/local/bin/python3

import sys,shelve,pyperclip
import re,os,shutil
import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - &(levelname)s - %(message)s')


def func(w1,w2,w3):
    return '{}時の{}は{}'.format(w1,w2,w3)

print(func('12','気温','22.5'))
