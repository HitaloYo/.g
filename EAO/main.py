from classes import Pessoa
def Main():
    x = str(input("NOME: "))
    y = str(input("Data de nascimento: "))
    z = str(input("Cpf: "))
    pessoa = Pessoa(x,y,z)

    print(pessoa.idade_pessoa(y))


if __name__ == '__main__':
    Main()

