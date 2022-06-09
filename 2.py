import re
a = open('quiz.docx','r')
baca = a.read()
sama = re.findall(r'\w+@\w+',baca)
print(sama)