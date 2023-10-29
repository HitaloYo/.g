def Menu():
    menu = '''
    Atividades // Trabalho // beecrownd
    Atividades(S) - 1
    trabalhos(F) - 1
    beecrownd(b) - 1007, 1008, 1010, 1011, 1012, 
    1013, 1014, 1015, 1019, 1020, 1021, 1036
    '''
    while True:
        try:
            print(menu)
            qual = input("Faculdade [f], Senac [s] ou Beecrownd[b]\n Resposta: ")
        except:
            continue
        try:
            atividade = int(input("Qual Atividade\n Atividade: "))
        except:
            continue
        else:
            if qual == "s" and atividade == 1:
                impar_par()
                media()
                negativo_positivo()
            elif qual == "f" and atividade == 1:
                estacionamento()
            elif qual == "b" and atividade == 1007:
                try:
                    b1007()
                except:
                    continue
            elif qual == "b" and atividade == 1008:
                try:
                    b1008()
                except:
                    continue
            elif qual == "b" and atividade == 1009:
                try:
                    b1009()
                except:
                    continue
            elif qual == "b" and atividade == 1010:
                try:
                    b1010()
                except:
                    continue
            elif qual == "b" and atividade == 1011:
                try:
                    b1011()
                except:
                    continue
            elif qual == "b" and atividade == 1012:
                try:
                    b1012()
                except:
                    continue
            elif qual == "b" and atividade == 1013:
                try:
                    b1013()
                except:
                    continue
            elif qual == "b" and atividade == 1014:
                try:
                    b1014()
                except:
                    continue
            elif qual == "b" and atividade == 1015:
                try:
                    b1015()
                except:
                    continue
            elif qual == "b" and atividade == 1016:
                try:
                    b1016()
                except:
                    continue
            elif qual == "b" and atividade == 1017:
                try:
                    b1017()
                except:
                    continue
            elif qual == "b" and atividade == 1018:
                try:
                    b1018()
                except:
                    continue
            elif qual == "b" and atividade == 1019:
                try:
                    b1019()
                except:
                    continue
            elif qual == "b" and atividade == 1020:
                try:
                    b1020()
                except:
                    continue
            elif qual == "b" and atividade == 1021:
                try:
                    b1021()
                except:
                    continue
            elif qual == "b" and atividade == 1035:
                try:
                    b1035()
                except:
                    continue
            elif qual == "b" and atividade == 1036:
                try:
                    b1036()
                except:
                    continue
            elif qual == "b" and atividade == 1037:
                try:
                    b1037()
                except:
                    continue
            elif qual == 0:
                break
#Atividade 1 - senac
def impar_par():
    #Questão 1 - senac
    print("Questão - 1")
    while True:
        try:
            numeros = input("Digite dois numeros: ").split()
            a, b = list(map(int,numeros))
        except:
            continue
        else:
            a_r = a % 2
            b_r = b % 2
            if a_r != 0 and b_r != 0:
                print("{} e {} são impares".format(a,b))
            elif a_r == 0 and b_r == 0:
                print("{} e {} são pares".format(a,b))
            elif a_r != 0 and b_r == 0:
                print("{} é impar e {} é par".format(a,b))
            elif a_r == 0 and b_r != 0:
                print("{} é par e {} é impar".format(a,b))
            break
def media():
    #Questão 2 - Senac
    print("Questão - 2")
    while True:
        try:
            numeros = input("Digite três notas: ").split()
            a, b, c = list(map(int, numeros))
        except:
            continue
        else:
            media = (a + b + c)/3
            if media >= 7:
                print("A media foi {:.2f}, O aluno está aprovado".format(media))
            elif media <= 7 and media >=5:
                print("A media foi {:.2f}, O aluno está recuperação".format(media))
            elif media < 5:
                print("A media foi {:.2f}, O aluno está reprovado".format(media))
            break
def negativo_positivo():
    print("Questão - 3")
    #Questão 3 - senac
    while True:
        try:
            a = float(input("Digite um numero: "))
        except:
            continue
        else:
            if a == 0:
                print("o numero é 0")
            elif a > 0:
                print("{:.0f} é positivo".format(a))
            elif a < 0:
                print("{:.0f} é negativo".format(a))
        break
                #FIM Atividade 1(Senac)
#Fim Atividade 1 - senac
#Beecrownd questões
def b1007():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    diferenca = a * b - c * d
    print("DIFERENCA =".format(diferenca))
def b1008():
    a = int(input())
    b = int(input())
    c = float(input())
    salary = b * c
    print("NUMBER = {}".format(a))
    print("SALARY = U$ {:.2f}".format(salary))
def b1009():
    a = str(input())
    b = float(input())
    c = float(input())
    print(f'TOTAL = R$ {b + ((c * 15) / 100):.2f}')

def b1010():
    linha1 = input().split()
    linha2 = input().split()
    x_1, y_1, z_1 = list(map(int, linha1))
    x_2, y_2, z_2 = linha2(map(int, linha2))
    resultado = (x_1 * y_1) + (x_2 * y_2)
    print("VALOR A PAGAR: R$ {:.2f}".format(resultado))
def b1011():
    N = int(input())
    area = (4 / 3) * 3.14159 * (N ** 3)
    print("VOLUME = {:.3f}".format(area))
def b1012():
    linha = input().split()
    a, b, c = list(map(int, linha))
    triangulo = (a * c) / 2
    circulo = (c * c) * 3.14159
    trapezio = ((a * c) / 2) + ((b * c) / 2)
    quadrado = b * b
    retangulo = a * b
    print("Resultados abaixo")
    print("TRIANGULO: {0:.3f}".format(triangulo))
    print("CIRCULO: {0:.3f}".format(circulo))
    print("TRAPEZIO: {0:.3f}".format(trapezio))
    print("QUADRADO: {0:.3f}".format(quadrado))
    print("RETANGULO: {0:.3f}".format(retangulo))
def b1013():
    linha = input().split()
    a, b, c = list(map(int, linha))
    maiorABC = (((a + b + abs(a - b))/2) + c + abs(((a + b + abs(a - b))/2) - c))/2
    print("{} eh o maior".format(int(maiorABC)))
def b1014():
    x = int(input())
    y = float(input())
    gasto = x/y
    print("{:.3f} km/l".format(gasto))
def b1015():
    linha = input().split()
    linha2 = input().split()
    x1, y1 = list(map(float, linha))
    x2, y2 = list(map(float, linha2))
    distancia = (((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))) ** 0.5
    print("{0:.4f}".format(distancia))
def b1016():
    y = int(input())
    y = y * 2
    print("{} minutos".format(y))
def b1017():
    tempo = int(input())
    velocidade = int(input())

    consumo = (tempo * velocidade) / 12

    print("{0:.3f}".format(consumo))
def b1018():
    n = int(input())
    notas = [100, 50, 20, 10, 5, 2, 1]
    print(n)
    for i in range(len(notas)):
        if (n >= notas[i]):
            print("%d nota(s) de R$ %d,00" % (n // notas[i], notas[i]))
            n = n % notas[i]
        else:
            print("0 nota(s) de R$ %d,00" % (notas[i]))
def b1019():
    N = int(input())
    horas = 0
    minutos = 0
    if N < 60:
        segundos = N
    elif N >= 60:
        segundos = int(N % 60)
        minutos = int(N / 60)
    if minutos >=60:
        horas = int(minutos / 60)
        minutos = int(minutos % 60)
    print("{}:{}:{}".format(horas, minutos, segundos))
def b1020():
    N = int(input())
    ano = N / 365
    ano = int(ano)
    resto_ano =  N % 365
    mes = resto_ano / 30
    mes = int(mes)
    dia = resto_ano % 30
    print("{} ano(s)".format(ano))
    print("{} mes(es)".format(mes))
    print("{} dia(s)".format(dia))
def b1021():
    n = float(input())
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01];

    print('NOTAS:')
    for i in range(len(notas)):
        qt = 0
        while n-notas[i] >= 0:
            qt += 1
            n -= notas[i]
        print("%d nota(s) de R$ %.2f" % (qt, notas[i]))

    print('MOEDAS:')

    for i in range(len(moedas)):
        qt = 0
        while n-moedas[i] >= 0:
            qt += 1
            n = float(format(round(n - moedas[i],2)))

        print("%d moeda(s) de R$ %.2f" % (qt, moedas[i]))
def b1035():
    linha = input().split()
    a, b, c, d = list(map(int, linha))
    if (b > c and d > a and (a + b) > (c + d) and c >= 0 and d >= 0 and a % 2 == 0):
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")
def b1036():
    linha = input().split()
    a, b, c = list(map(float, linha))
    delta = (b*b)-4 * a * c
    raizdelta = delta ** 0.5
    if(a == 0.0 or delta < 0.0):
        print("Impossivel calcular")
    else:
        r1 =((-b) + raizdelta)/(2*a)
        r2 =((-b) - raizdelta)/(2*a)
        print("R1 = {:.5f}".format(r1))
        print("R2 = {:.5f}".format(r2))
    n = float(input())
    if n >= 0 and n <= 25:
        print("Intervalo (0,25]")
    elif n >= 25 and n <= 50:
        print("Intervalo (25,50]")
    elif n >= 50 and n <= 75:
        print("Intervalo (50,75]")
    elif n >= 75 and n <= 100:
        print("Intervalo (75,100]")
    else:
        print("Fora de intervalo")
def b1037():
    x = float(input())
    if 0 <= x <= 25:
        print('Intervalo [0,25]')
    if 25 < x <= 50:
        print('Intervalo (25,50]')
    if 50 < x <= 75:
        print('Intervalo (50,75]')
    if 75 < x <= 100:
        print('Intervalo (75,100]')
    if x > 100 or x < 0:
        print('Fora de intervalo')
#fim beecrownd
#trabalho facul
#auciono
def estacionamento():
    #/////////////////////##/////////////////////##/////////////////////#
    chegada = input("Horario da chegada: 'Horas e minutos': ").split()
    saida = input("Horario da saida: 'Horas e minutos': ").split()
    hora_chegada, min_chegada = list(map(int, chegada))
    hora_saida, min_saida = list(map(int, saida))
    #/////////////////////##/////////////////////##/////////////////////#
    #Calculo das horas
    hora = hora_chegada - hora_saida
    hora_pos = abs(hora)
    min = min_chegada - min_saida
    min_pos = abs(min)
    #/////////////////////##/////////////////////##/////////////////////#
    #variaveis fixas#
    valor = 5
    multa = 1
    total = 0
    #/////////////////////##/////////////////////##/////////////////////#
    #descobrindo a hora exata e convertendo para minutos
    if hora > 0:
        hora_f = 24 - hora
    elif hora < 0:
        hora_f = abs(hora)
    else:
        hora_f = 0
    aux_min = hora_f * 60
    #/////////////////////##/////////////////////##/////////////////////#
    #descobrindo os minutos exatas e somando com os minutos das horas
    if min < 0:
        min_f = abs(min) + aux_min
    elif min > 0:
        min_f = min + aux_min
    else:
        min_f = 0 + aux_min
    #/////////////////////##/////////////////////##/////////////////////#
    #calculando o total
    if min_f <= 60 and min_f > 0:
        total = valor
    elif min_f <= 120 and min_f > 60:
        total = valor * 2
    elif min_f > 120:
        aux = min_f/60
        aux_2 = min_f%60
        if aux > 2:
            if aux_2 > 0:
                aux = int(aux)
                aux = aux + 1
                total = (aux * valor) + (multa * (aux - 2))
            else:
                aux = int(aux)
                total = (aux * valor) + (multa * (aux - 2))
    #/////////////////////##/////////////////////##/////////////////////#
    #resposta
    print("o carro ficou estacionado por {} horas e {} minutos, vai pagar o total de {:.2f} R$".format(hora_pos, min_pos, total))
#auciono
#fim trabalho facul
