import os
#lst = os.listdir(path)
#for root, dirs, files in os.walk(path):
    #for file in files:
        #if not file.endswith ('.txt'):
            #continue
        #f = open(root + os.sep + file, 'r')
def explore_folders():
    directories = []
    for root, dirs, files in os.walk('Desktop'):
        for folder in dirs:
            if 'r' in folder:
                directories.append(folder)
    return directories

def explore_files(directory):
    filenames = []
    for roots, dirs, files in os.walk(directory):
        for fl in files:
            if 'd' in fl:
                filenames.append(fl)
    return filenames

def main():
    len1 = len(explore_folders())
    print(len1)
    len2 = len(explore_files('Desktop'))
    print(len2)
    for item in explore_folders():
        print(explore_files(item))

main()
