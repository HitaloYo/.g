def Menu():
    menu = '''
    Atividades // Trabalho
    Atividades(S) - 1
    Atividades(F) - 0
    trabalhos(S) - 0
    trabalhos(F) - 0
    beecrownd(b) - 1019, 1020
    '''
    while True:
        try:
            print(menu)
            qual = input("Faculdade [f] ou Senac [s]\n Resposta: ")
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
            elif qual == "b" and atividade == 1019:
                b1019()
            elif qual == "b" and atividade == 1020:
                b1020()
            elif q == 0:
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
N = float(input)




