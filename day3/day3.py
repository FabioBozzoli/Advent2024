with open('input.txt', 'r') as f:
  lines = f.readlines()

#TASK 1
somma = 0
mul = True
for i in lines:
    stringa_rimanente = i
    mul = True
    while(mul):
        numero_1 = stringa_rimanente[stringa_rimanente.find("mul(") + 4:].split(",")[0]
        numero_2 = stringa_rimanente[stringa_rimanente.find("mul(") + 4:].split(",")[1].split(")")[0]
        if numero_1.isdigit() and numero_2.isdigit():
            somma += (int)(numero_1) * (int)(numero_2)
            lung_substr = len("mul("+(str)(numero_1)+","+(str)(numero_2)+")")
            stringa_rimanente = (str)(stringa_rimanente[stringa_rimanente.find("mul(")+4:])
        elif(not numero_1.isdigit()):
            stringa_rimanente = stringa_rimanente[stringa_rimanente.find("mul(") + 4:]
        elif(not numero_2.isdigit()):
            stringa_rimanente = stringa_rimanente[stringa_rimanente.find("mul(") + 4:]
        if(stringa_rimanente.find("mul(") == -1):
            mul = False


  #TASK 2
  def mul(stringa):
    somma = 0
    stringa_rimanente = stringa
    mul = True
    while(mul):
        lista = stringa_rimanente[stringa_rimanente.find("mul(") + 4:].split(",")
        if stringa_rimanente.find("mul(") != -1 and len(lista) > 1:
            numero_1 = stringa_rimanente[stringa_rimanente.find("mul(") + 4:].split(",")[0]
            numero_2 = stringa_rimanente[stringa_rimanente.find("mul(") + 4:].split(",")[1].split(")")[0]
            if numero_1.isdigit() and numero_2.isdigit():
                print(numero_1 + "," + numero_2)
                somma += (int)(numero_1) * (int)(numero_2)
                lung_substr = len("mul("+(str)(numero_1)+","+(str)(numero_2)+")")
                stringa_rimanente = (str)(stringa_rimanente[stringa_rimanente.find("mul(")+4:])
            elif(not numero_1.isdigit()):
                stringa_rimanente = stringa_rimanente[stringa_rimanente.find("mul(") + 4:]
            elif(not numero_2.isdigit()):
                stringa_rimanente = stringa_rimanente[stringa_rimanente.find("mul(") + 4:]
        else:
            mul = False
    return somma


output = 0
stringa_rimanente = ""
for i in lines:
    stringa_rimanente += i

controllo = True
while(controllo):
    first_do = stringa_rimanente.find("do()")
    first_dont = stringa_rimanente.find("don't()")

    print(stringa_rimanente)

    if(first_do == -1 and first_dont == -1):
        output += mul(stringa_rimanente)
        controllo = False
    elif(first_do == -1):
        output += mul(stringa_rimanente[:first_dont])
        controllo = False
    elif(first_dont == -1):
        output += mul(stringa_rimanente)
        controllo = False
    elif(first_do < first_dont):
        output += mul(stringa_rimanente[:first_dont])
        stringa_rimanente = stringa_rimanente[first_dont:]
    elif(first_do > first_dont):
        output += mul(stringa_rimanente[:first_dont])
        stringa_rimanente = stringa_rimanente[first_do:]
