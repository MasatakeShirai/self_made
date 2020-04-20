#キャッシュを残さない
import sys
sys.dont_write_bytecode = True

from LaunchDeepL import LaunchDeepL
from StringMold import StringMoldForDeepL
import os

os.chdir('UseDeepL')

file = open('before.txt', 'r')
string = file.read()
file.close()

Mold_String = StringMoldForDeepL(string)

file = open('after.txt', 'w')
file.write(StringMoldForDeepL(string))
file.close()

LaunchDeepL(Mold_String)
