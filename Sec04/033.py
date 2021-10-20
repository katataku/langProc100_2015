# -*- coding: utf8 -*-
import MeCab
import re
import codecs

def set_dic(text,dic_list):
    tagger = MeCab.Tagger("")
    result = tagger.parse(text)
    for line in result.splitlines():     
        if line == 'EOS':
            break
        if len(line.split()) != 2:
            continue
        dic = {}
        l =line.split()
#        print(l)
        surface = l[0]
        rem = l[1].split(',')
        base = rem[6]
        pos = rem[0]
        pos1 = rem[1]

        dic.setdefault("surface",surface)
        dic.setdefault("base",base)
        dic.setdefault("pos",pos)
        dic.setdefault("pos1",pos1)
        dic_list.append(dic)



#text = 'メロスは激怒した。必ず、かの邪智暴虐じゃちぼうぎゃくの王を除かなければならぬと決意した。メロスには政治がわからぬ。メロスは、村の牧人である。'
file = codecs.open('./neko.txt','r','utf-8' )
text = file.read()
dic_list = []
set_dic(text,dic_list) 

for dic in dic_list[:10]:
    if dic["pos"] == "名詞":
        print('base : {}, pos1 : {}'.format(dic["base"],dic["pos1"]))

    
