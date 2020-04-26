#キャッシュを残さない
import sys
sys.dont_write_bytecode = True

from LaunchDeepL import LaunchDeepL
from StringMold import StringMoldForDeepL, StringMoldForPaste
import pyperclip

import os
import getopt
import sys

#スクリプト名以外の引数を取得
argv =sys.argv[1:]

os.chdir('UseDeepL')

file = open('before.txt', 'r')
string = file.read()
file.close()

Mold_String = StringMoldForDeepL(string)
LaunchDeepL(Mold_String)
translate_string = StringMoldForPaste(pyperclip.paste())
pyperclip.copy(translate_string)

file = open('after.txt','w',encoding='utf-8')
file.write(translate_string)
file.close()
