import os
os.chdir('StringMoldForDeepL')

file = open('before.txt', 'r')
string = file.read()
file.close()

mold_string = string.replace('\n',' ').replace('. ','.\n').replace(' rst',' first').replace(' nd', ' find')

file = open('after.txt', 'w')
file.write(mold_string)
file.close()
