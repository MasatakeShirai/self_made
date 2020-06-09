import os

os.chdir("LengthOfSentence")

file = open('target.txt', 'r', encoding='utf-8')

s = file.read().replace('\n','')

print(len(s))

file.close()
