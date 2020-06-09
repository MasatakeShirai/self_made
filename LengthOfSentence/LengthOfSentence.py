import os

os.chdir("LengthOfSentence")

file = open('target.txt', 'r', encoding='utf-8')
print(file.readline())
file.close()
