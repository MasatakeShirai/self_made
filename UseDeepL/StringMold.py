import os

def StringMoldForDeepL(string):
    #文字列を整形する    
    mold_string = string.replace('\n',' ').replace('. ','.\n').replace('','fi').replace('','fl').replace('','ff')
 
    return mold_string

def StringMoldForPaste(string):
    mold_string = string.replace('\r\n','').replace('|','\n')
    return mold_string

if __name__ == "__main__":
    os.chdir('UseDeepL')
    file = open('after.txt', 'r', encoding='utf-8')
    string = file.read()
    file.close()

    moldstring = StringMoldForPaste(string)

    file = open('after.txt', 'w', encoding='utf-8')
    file.write(moldstring)
    file.close()
