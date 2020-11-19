#Creo un valor para guardar el byte
digito = ""

#Funcion para transformar un digito de hexadecimal en su correspondiente byte
def binario(num, base):
    global digito
    digito += str(num%base)
    if num == 1 or num == 0:
        return num
    return binario(num//base, base)

#Funcion para transformar toda una palabra de hexadecimal a binario
def hexBin(numero):
    global digito
    total = ""
    aux = ""
    valoresnum = "0123456789"
    for i in range(len(numero)):
        if numero[i] in valoresnum:
            binario(int(numero[i]), 2)
            if len(digito) < 4:
                digito += "0"*(4-len(digito))
            total += digito[::-1]
        elif numero[i] == "a":
            binario(10, 2)
            if len(digito) < 4:
                digito += "0"*(4-len(digito))
            total += digito[::-1]
        elif numero[i] == "b":
            binario(11, 2)
            if len(digito) < 4:
                digito += "0"*(4-len(digito))
            total += digito[::-1]
        elif numero[i] == "c":
            binario(12, 2)
            if len(digito) < 4:
                digito += "0"*(4-len(digito))
            total += digito[::-1]
        elif numero[i] == "d":
            binario(13, 2)
            if len(digito) < 4:
                digito += "0"*(4-len(digito))
            total += digito[::-1]
        elif numero[i] == "e":
            binario(14, 2)
            if len(digito) < 4:
                digito += "0"*(4-len(digito))
            total += digito[::-1]
        else:
            binario(15, 2)
            if len(digito) < 4:
                digito += "0"*(4-len(digito))
            total += digito[::-1]
        digito = ""
    return total

#Convierto cada instruccion y la separo en sus grupos
def convertir(todo):
#Creo las columnas
    op = []
    tipo = []
    rs = []
    rt = []
    rd = []
    shamt = []
    funct = []
    imm = []
    bits = ""                         #Variable para guardar los primeros 6 bits (el opcode)
    instrucciones = todo.split(" ")   #Guardo los distintos valores en un arreglo
    traduccion = []                   #Arreglo para guardar la traduccion en bits de los valores
    for i in range(len(instrucciones)):
        traduccion.append(hexBin(instrucciones[i]))
    for i in traduccion:
        for bit in range(6):
           bits += i[bit]
        op.append(bits)
        bits = ""
    #Diferencio entre R e I (Si el opcode es distinto de 000000, entonces es I. Sino, es R)
    for i in op:
        if i == "000000":
            tipo.append("  R  ")
        else:
            tipo.append("  I  ")
    #Asigno los valores de las columnas rs, rt (cuyo atron es igual en todos), rd, shamt, funct y imm
    #dependiendo del tipo de instruccion que sea
    for i in range(len(tipo)):
        rs.append(traduccion[i][6:11])
        rt.append(traduccion[i][11:16])
        if tipo[i] == "  I  ":
            rd.append("NA   ")
            shamt.append("NA   ")
            funct.append("NA    ")
            imm.append(traduccion[i][16:32])
        else:
            rd.append(traduccion[i][16:21])
            shamt.append(traduccion[i][21:26])
            funct.append(traduccion[i][26:32])
            imm.append("NA              ")
    #Imprimo la tabla con los datos
    print("|instrucc| tipo|  op  |  rs |  rt |  rd |shamt|funct |       imm      |")
    for i in range(len(instrucciones)):
        print("|" + instrucciones[i] + "|" + tipo[i] + "|" + op[i] + "|" + rs[i] + "|" + rt[i] + "|" + rd[i] + "|" + shamt[i] + "|" + funct[i] + "|" + imm[i] + "|", end = "\n")
print("""
Este es un programa pensado para traducir valores de instrucciones de MIPS y separar sus elementos
-op-rs-rt-rd-shamt-funct-imm- y mostrar el tipo de instruccion que es.
Para poner los valores solo escribalos con una separacion, por ejemplo:
34020004 3c041001 0000000c ....
""")

convertir(input("Ingrese los valores de las instrucciones: "))


