import MeCab
import re


def set_dic(text,dic_list):
    tagger = MeCab.Tagger("")
    result = tagger.parse(text)
    for line in result.splitlines():     
        if line == 'EOS':
            break
        dic = {}
        l =line.split()
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

#    print('surface = {}, base = {}, pos = {}, pos1 = {}'.format(surface,base,pos,pos1))

text = 'メロスは激怒した。必ず、かの邪智暴虐じゃちぼうぎゃくの王を除かなければならぬと決意した。メロスには政治がわからぬ。メロスは、村の牧人である。'
dic_list = []
set_dic(text,dic_list) 

for dic in dic_list:
    if dic["pos"] == "動詞":
        print(dic["surface"])

    
