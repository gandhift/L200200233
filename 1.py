import re
x = input('masukkan username :')
y = '[@]+[a-zA-Z]+[0-9]'
if re.findall(y,x):
    print('pass')
else:
    print('failed')