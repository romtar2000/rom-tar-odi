import re

def readfile(file):
    with open(file, encoding="utf-8") as f:
        text = f.read()
    return text

def substitute(text):
    new_text = re.sub('комар([ауоеы]?)([мвх]?)(и)?', 'слон\1\2\3', text)
    return new_text

def rewrite(file, text):
    with open(file, 'w', encoding = "utf-8") as f:
        f.write(text)

def main():
    rewrite("mosquitos.html", substitute(readfile("mosquitos.html")))

main()
