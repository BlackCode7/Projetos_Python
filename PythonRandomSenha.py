#!/usr/bin/python

import random

lower = 'abcdefjhijlmnopqrstuvwxyz'
upper = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "{}[]:;/*+|!@#$%^&~"
all = lower+upper+number+symbol

# definindo o numero de caracteres
lenght = 24

# mixando os caracteres e definindo o tamanho em números
password = ''.join(random.sample(all, lenght))

listaPassword = []

listaPassword.append(password)

print(password)
print(listaPassword)



aList = [123, 'xyz', 'zara', 'abc'];
aList.append( password );
print("Updated List : ", aList)

# A6YrzjU3iuFad79oJvch8&l^
# c0+{]2SxZOD&I@Ce5v1#:NWuq
# Va96O#/xT;J0j}~WQ:h[8M34

# play list youtube
# https://youtu.be/qFLhGq0060w