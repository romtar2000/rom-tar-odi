import re

def readfile(file):
    with open(file, encoding="utf-8") as f:
        code = f.read()
        return code
    
def search(code):
    result = re.search(r'Столица[\s\S]*?title="(.*)"',code)
    capital = ''.join(result.group(1))
    return capital

def write_in_file(text):
    with open("answer.txt", "w", encoding="utf-8") as f:
        f.write(text)

write_in_file(search(readfile("Zambia.txt")))
