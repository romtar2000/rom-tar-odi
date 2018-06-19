import os
import re

def fileslist():
    kartoteka = os.listdir('.')
    return kartoteka

def readfiles(kartoteka):
    texts = []
    for file in kartoteka:
        with open(file, encoding="utf-8") as f:
            text = f.read()
            texts.append(text)
    return texts

def maketable(text_list):
    for text in text_list:
        data1 = re.search('meta content="(.*)" name="docid"', text)
        if data1:
            docid = data1.group(1)
        data2 = re.search('<title>(.*)</title>', text)
        if data2:
            title = data2.group(1)
        data3 = re.search('meta content="(.*)" name="author"', text)
        if data3:
            author = data3.group(1)
        data4 = re.search('meta content="(.*)" name="created"', text)
        if data4:
            created = data4.group(1)
        data5 = re.search('meta content="(.*)" name="topic"', text)
        if data5:
            topic = data5.group(1)
        data6 = re.search('meta content="(.*)" name="tagging"', text)
        if data6:
            tagging = data6.group(1)
        print(docid + "," + title + "," + author + "," + created + "," + topic + "," + tagging)
                
def searchabb(text_list):
    freqdict = {}
    fullist = []
    for text in text_list:
        answer = re.findall("[/s]([А-ЯЁA-Z]).+^[а-яёa-z][/s]", text)
        for item in answer:
            fullist.append(item)
    for element in fullist:
        if element in freqdict:
            freqdict[element] = freqdict[element] + 1
        else:
            freqdict[element] = 1
    for key, value in freqdict.items():
        print(key)
        print("\t")
        print(value)
       

    
def main():
   maketable(readfiles(fileslist()))
   searchabb(readfiles(fileslist()))

main()

