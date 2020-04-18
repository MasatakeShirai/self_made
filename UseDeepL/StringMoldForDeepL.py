def StringMoldForDeepL(string):    
    mold_string = string.replace('\n',' ').replace('. ','.\n').replace('','fi')
    return mold_string

import os
os.chdir('UseDeepL')

file = open('before.txt', 'r')
string = file.read()
file.close()

file = open('after.txt', 'w')
file.write(StringMoldForDeepL(string))
file.close()
