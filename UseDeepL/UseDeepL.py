#キャッシュを残さない
import sys
sys.dont_write_bytecode = True

from LaunchDeepL import LaunchDeepL
from StringMold import StringMoldForDeepL, StringMoldForPaste
import pyperclip

import os
import getopt
import sys
import re

#スクリプト名以外の引数を取得
argv =sys.argv[1:]
options, arguments = getopt.getopt(argv, "hg", ["help", "generate"])

#option_dictはオプションによる設定のまとめ
option_dict = {'help':False, 'generate':[False,'after.txt']}

#引数を読んで，option_dictのフラグを立てる
for name,value in options:
    if name in ('-h','--help'):
        option_dict['help'] = True
    if name in ('-g','--generate'):
        option_dict['generate'][0] = True
        text_pattern = re.compile('[a-zA-Z0-9]*.txt')
        for arg in arguments:
            if text_pattern.match(arg):
                option_dict['generate'][1] = arg
                break            
            
#ヘルプを表示する
if option_dict['help']:
    print('before.txtに英文を保存してこのスクリプトを実行すると，DeepLのサイトをスクレイピングして翻訳をクリップボードにコピーします．')
    print('英文に|を挿入すると，訳文のその部分を改行できます．\r\n')
    print('-g, --generate: after.txtに翻訳結果を出力します．txtファイルの名前を指定すると，そのファイルに結果を出力します．')
    sys.exit()

os.chdir('UseDeepL')
    
file = open('before.txt', 'r', encoding='utf-8')
string = file.read()
file.close()

Mold_String = StringMoldForDeepL(string)
LaunchDeepL(Mold_String)
translate_string = StringMoldForPaste(pyperclip.paste())
pyperclip.copy(translate_string)

#結果をtxtファイルに出力する
if option_dict['generate'][0]:
    file = open(option_dict['generate'][1],'w',encoding='utf-8')
    file.write(translate_string)
    file.close()
