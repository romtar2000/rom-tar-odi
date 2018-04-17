import os
import re

def search_numberfiles():
    answer = []
    kartoteka = os.listdir()
    for item in kartoteka:
        if os.path.isfile(item):
            if re.search ('[0123456789]', item):
                answer.append(item)
    print(len(answer))

def make_catalog():
    catalog = {}
    kartoteka = os.listdir()
    for item in kartoteka:
        if os.path.isfile(item) or os.path.isdir(item):
            if item in catalog:
                catalog[item] = catalog[item] + 1
            else:
                catalog[item] = 1
    for k in catalog:
        print(k)
        
def main():
    search_numberfiles()
    make_catalog()

main()
        
