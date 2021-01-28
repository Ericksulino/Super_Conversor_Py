#função para converter celcius em fahrenheit:
def Cf(c):
    f=c*(9.0/5.0)+32
    return f

#função para converter fahrenheit em celcius:
def Fc(f):
    c=5.0*(f-32)/9
    return c

#função para converter kelvin em celcius:
def Kc(k):
    c=k-273.15
    return c

#função para converter celcius em kelvin:
def Ck(c):
    k=c+273.15
    return k

#função para converter quilometros em metros por segundo:
def KmM(k):
    ms = k/3.6
    return ms

#função para converter metros por segundo em quilometros:
def MsK(ms):
    kh = ms*3.6
    return kh

#função para converter milhas em quilometros:
def Mkm(m):
    km = m*1.61
    return km

#função para converter quilometros em  milhas:
def Kmmi(k):
    m = k/1.61
    return m

#função para converter graus em  radianos:
def Gr(g):
    pi=3.14
    r=g*pi/180
    return r

#função para converter radianos em graus:
def Rg(r):
    pi=3.14
    g=r*180/pi
    return g

#função para converter polegadas em centimetros:
def Pc(p):
    c=p*2.54
    return c

#função para converter centimetros em polegadas:
def Cp(c):
    p=c/2.54
    return p

#função para converter metros cubicos em litros:
def M3l(m):
    l = m*1000
    return l

#função para converter litros em metros cubicos:
def Lm3(l):
    m=l/1000
    return m

#função para converter quilograms em libras:
def Kgl(k):
    l = k/0.45
    return l

#função para converter libras em quilogramas:
def Lkg(l):
    k = l*0.45
    return k

#função para converter jardas em metros:
def Jm(j):
    m = j*0.91
    return m

#função para converter metros em jardas:
def Mj(m):
    j = m/0.91
    return j

#função para converter metros quadrados em acres:
def M2a(m2):
    ac = m2*0.000247
    return ac

#função para converter acres em metros quadrados:
def Acm(ac):
    m2 = ac*4048.58
    return m2

#função para converter metros quadrados em hectares:
def M2h(m2):
    he = m2*0.0001
    return he

#função para converter hectares em metros quadrados:
def Hem(he):
    m2 = he*0.10000
    return m2

#laço infinito para escolher o que vai ser covertido até que seja digitado "sair":
while True:
    print('Digite o que voce quer converter ou sair para sair:(ex: temperatura,area..)')
    op = input('------> ')
    if op == 'sair':
        break
    # caso a opção digitada seja temperatura devera ser escolhido o tipo de medida a ser convertida
    # e tambem sai do laço caso seja digitado "sair":
    elif op == 'temperatura':
        v = float(input('Digite o valor: '))
        print('Escreva de qual tipo e o valor que voce vai escrever (ex: fah para fahrenheit,cel para celcius..)')
        de = input('------> ')
        if de == 'sair':
            break
        print('Agora o tipo que voce quer converter:(ex: fah para fahrenheit,cel para celcius..)')
        pr = input('------> ')
        if pr == 'sair':
            break
        elif de == 'cel' and pr == 'fah':
            re=Cf(v)
        elif de == 'fah' and pr == 'cel':
            re=Fc(v)
        elif de == 'kel' and pr == 'cel':
            re=Kc(v)
        elif de == 'cel' and pr == 'kel':
            re=Ck(v)
        #opção caso não seja digitado nenhuma palavra existente nos ifs:
        else:
            print('Invalido!! Digite novamente por favor!!')
    
    # caso a opção digitada seja velocidade devera ser escolhido o tipo de medida a ser convertida
    # e tambem sai do laço caso seja digitado "sair":
    elif op == 'distancia':
        v = float(input('Digite o valor: '))
        print('Escreva de qual tipo e o valor que voce vai escrever (ex: mi para milhas,km para kilometros)')
        de = input('------> ')
        if de == 'sair':
            break
        print('Agora o tipo que voce quer converter:(ex: mi para milhas,km para kilometros)')
        pr = input('------> ')
        if pr == 'sair':
            break
        elif de == 'mi' and pr == 'kh':
            re=MsK(v)
        elif de == 'kh' and pr == 'mi':
            re=Kmmi(v)

        #opção caso não seja digitado nenhuma palavra existente nos ifs:
        else:
            print('Invalido!! Digite novamente por favor!!')

    # caso a opção digitada seja distancia devera ser escolhido o tipo de medida a ser convertida
    # e tambem sai do laço caso seja digitado "sair":
    elif op == 'velocidade':
        v = float(input('Digite o valor: '))
        print('Escreva de qual tipo e o valor que voce vai escrever (ex: ms para metros por segundo,km para kilometros por hora )')
        de = input('------> ')
        if de == 'sair':
            break
        print('Agora o tipo que voce quer converter:(ex: ms para metros por segundo,km para kilometros por hora )')
        pr = input('------> ')
        if pr == 'sair':
            break
        elif de == 'ms' and pr == 'kh':
            re=Mkm(v)
        elif de == 'kh' and pr == 'ms':
            re=KmM(v)

        #opção caso não seja digitado nenhuma palavra existente nos ifs:
        else:
            print('Invalido!! Digite novamente por favor!!')
    
    # caso a opção digitada seja area devera ser escolhido o tipo de medida a ser convertida
    # e tambem sai do laço caso seja digitado "sair":
    elif op == 'area':
        v = float(input('Digite o valor: '))
        print('Escreva de qual tipo e o valor que voce vai escrever (ex: m2 para metros por quadrados,he para hectares...)')
        de = input('------> ')
        if de == 'sair':
            break
        print('Agora o tipo que voce quer converter:(ex: m2 para metros por quadrados,he para hectares...)')
        pr = input('------> ')
        if pr == 'sair':
            break
        elif de == 'm2' and pr == 'ac':
            re=M2a(v)
        elif de == 'ac' and pr == 'm2':
            re=Acm(v)
        elif de == 'm2' and pr == 'he':
            re=M2h(v)
        elif de == 'he' and pr == 'm2':
            re=Hem(v)
        
        #opção caso não seja digitado nenhuma palavra existente nos ifs:
        else:
            print('Invalido!! Digite novamente por favor!!')

    # caso a opção digitada seja angulo devera ser escolhido o tipo de medida a ser convertida
    # e tambem sai do laço caso seja digitado "sair":
    elif op == 'angulo':
        v = float(input('Digite o valor: '))
        print('Escreva de qual tipo e o valor que voce vai escrever (ex: g para graus,r para radianos)')
        de = input('------> ')
        if de == 'sair':
            break
        print('Agora o tipo que voce quer converter:(ex: g para graus,r para radianos)')
        pr = input('------> ')
        if pr == 'sair':
            break
        elif de == 'g' and pr == 'r':
            re=Gr(v)
        elif de == 'r' and pr == 'g':
            re=Rg(v)

        #opção caso não seja digitado nenhuma palavra existente nos ifs:
        else:
            print('Invalido!! Digite novamente por favor!!')


    # caso a opção digitada seja comprimento devera ser escolhido o tipo de medida a ser convertida
    # e tambem sai do laço caso seja digitado "sair":
    elif op == 'comprimento':
        v = float(input('Digite o valor: '))
        print('Escreva de qual tipo e o valor que voce vai escrever (ex: cm para centimetros,pol para polegadas...)')
        de = input('------> ')
        if de == 'sair':
            break
        print('Agora o tipo que voce quer converter:(ex: cm para centimetros,p para polegadas...)')
        pr = input('------> ')
        if pr == 'sair':
            break
        elif de == 'cm' and pr == 'pol':
            re=Cp(v)
        elif de == 'pol' and pr == 'cm':
            re=Pc(v)
        elif de == 'jar' and pr == 'm':
            re=Jm(v)
        elif de == 'm' and pr == 'jar':
            re=Mj(v)

        #opção caso não seja digitado nenhuma palavra existente nos ifs:
        else:
            print('Invalido!! Digite novamente por favor!!')

    # caso a opção digitada seja volume devera ser escolhido o tipo de medida a ser convertida
    # e tambem sai do laço caso seja digitado "sair":    
    elif op == 'volume':
        v = float(input('Digite o valor: '))
        print('Escreva de qual tipo e o valor que voce vai escrever (ex: l para litros,m3 para metros cubicos)')
        de = input('------> ')
        if de == 'sair':
            break
        print('Agora o tipo que voce quer converter:(ex: l para litros,m3 para metros cubicos)')
        pr = input('------> ')
        if pr == 'sair':
            break
        elif de == 'l' and pr == 'm3':
            re=Lm3(v)
        elif de == 'm3' and pr == 'l':
            re=M3l(v)
        
        #opção caso não seja digitado nenhuma palavra existente nos ifs:
        else:
            print('Invalido!! Digite novamente por favor!!')
    
    # caso a opção digitada seja massa devera ser escolhido o tipo de medida a ser convertida
    # e tambem sai do laço caso seja digitado "sair":
    elif op == 'massa':
        v = float(input('Digite o valor: '))
        print('Escreva de qual tipo e o valor que voce vai escrever (ex: kg para quilogramas,lib para libras)')
        de = input('------> ')
        if de == 'sair':
            break
        print('Agora o tipo que voce quer converter:(ex: kg para quilogramas,l para libras)')
        pr = input('------> ')
        if pr == 'sair':
            break
        elif de == 'lib' and pr == 'kg':
            re=Kgl(v)
        elif de == 'kg' and pr == 'lib':
            re=Lkg(v)
        
        #opção caso não seja digitado nenhuma palavra existente nos ifs:
        else:
            print('Invalido!! Digite novamente por favor!!')
    
    #opção caso não seja digitado nenhuma palavra existente nos ifs:
    else:
        print('Invalido!! Digite novamente por favor!!')

    print(f'Esse e o valor da corversao de  {de} para {pr} : {re:.2f}')


'''
    Algoritmo desenvolvido por Ericksulino Moura no dia 19/03/2020
    na quarentena do novo corona vírus, feito com a finalidade de exercitar
    a linguagem python. 
'''