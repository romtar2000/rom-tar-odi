import os

def count_depth():
    start_path = '.'
    depthlist = []
    for root, dirs, files in os.walk(start_path):
        rootroot = root.split(os.sep)
        rootroot_clean = rootroot[1::]
        depth = len(rootroot_clean)
        depthlist.append(depth)
    answer = max(depthlist)
    return answer

def main():
    print(count_depth())

main()

            
    
    
    
    


        
