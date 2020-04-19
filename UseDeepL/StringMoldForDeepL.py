import os


def StringMoldForDeepL(string):
    #文字列を整形する    
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
