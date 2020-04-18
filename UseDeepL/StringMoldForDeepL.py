import os
import sys

def StringMoldForDeepL(string):
    #キャッシュを残さない
    sys.dont_write_bytecode = True
    #文字列を加工する    
    mold_string = string.replace('\n',' ').replace('. ','.\n').replace('','fi').replace('','fl')
 
    return mold_string

if __name__ == "__main__":
    os.chdir('UseDeepL')

    file = open('before.txt', 'r')
    string = file.read()
    file.close()

    file = open('after.txt', 'w')
    file.write(StringMoldForDeepL(string))
    file.close()
