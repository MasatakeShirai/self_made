#キャッシュを残さない
import sys
sys.dont_write_bytecode = True

from LaunchDeepL import LaunchDeepL
from StringMold import StringMoldForDeepL, StringMoldForPaste
import pyperclip

import os

os.chdir('UseDeepL')

file = open('before.txt', 'r')
string = file.read()
file.close()

Mold_String = StringMoldForDeepL(string)
LaunchDeepL(Mold_String)

file = open('after.txt', 'w', encoding='utf-8')
file.write(pyperclip.paste())
file.close()

file = open('after.txt', 'r', encoding='utf-8')
s = file.read()
file.close()

translate_string = StringMoldForPaste(s)
pyperclip.copy(translate_string)
