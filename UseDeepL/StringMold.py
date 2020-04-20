import os

def StringMoldForDeepL(string):
    #文字列を整形する    
    mold_string = string.replace('\n',' ').replace('. ','.\n').replace('','fi').replace('','fl')
 
    return mold_string

def StringMoldForPaste(string):
    mold_string = string.replace('\n','').replace('|','\n')
    return mold_string

if __name__ == "__main__":
    os.chdir('UseDeepL')

    print(StringMoldForPaste('あいう|えお'))
