import os
os.chdir('StringMoldForDeepL')

file = open('before.txt', 'r')
string = file.read()
file.close()

print(string)

file = open('after.txt', 'w')
file.write(string)
file.close()
