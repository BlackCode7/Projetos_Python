from datetime import datetime


var1 = range(1, 60)

for i in var1:
    EsteMinuto = datetime.today().minute

    if EsteMinuto in var1:
        print(i, 'True')
    else:
        print(i, 'False')