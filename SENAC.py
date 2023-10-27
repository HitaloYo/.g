#Atividade 1
    #Q1
def imparoupar():
    numeros = input("Digite dois numeros: ").split()
    a, b = list(map(int,numeros))
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
    #Q2
def media():
    numeros = input("Digite três notas: ").split()
    a, b, c = list(map(int, numeros))
    media = (a + b + c)/3
    if media >= 7:
        print("A media foi {:.2f}, O aluno está aprovado".format(media))
    elif media <= 7 and media >=5:
        print("A media foi {:.2f}, O aluno está recuperação".format(media))
    elif media < 5:
        print("A media foi {:.2f}, O aluno está reprovado".format(media))
    #Q3
def negativo_positivo():
    a = float(input("Digite um numero: "))
    if a == 0:
        print("o numero é 0")
    elif a > 0:
        print("{:.0f} é positivo".format(a))
    elif a < 0:
        print("{:.0f} é negativo".format(a))
#FIM :0




