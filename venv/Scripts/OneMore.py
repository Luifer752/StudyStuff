import re

txt = str(input('Введите строку: '))


if re.match(r'^(?:0[1-9]|[1-2]\d|3[0-1])-(?:0[1-9]|1[0-2])-\d{4}$', txt):
    print('Valid')
else:
    print("Invalid")
