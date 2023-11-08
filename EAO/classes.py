class Pessoa:
    
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def idade_pessoa(self,data_nascimento):
        dia = int(data_nascimento.split("/")[0])
        mes = int(data_nascimento.split("/")[1])
        ano = int(data_nascimento.split("/")[2])
        
        ano_atual = 2023
        mes_atual = 11
        dia_atual = 8

        idade = ano_atual - ano
        if dia >= dia_atual and mes >= mes_atual:
            idade += 1  
        return idade
    
    def maior_de_idade(self):
        if self.data_nascimento > 17:
            return "È maior de idade"
        return "È menor de idade"
    
    def saudacao(self):
        return "Ola {}, você {} e tem {} anos".format(self.nome,self.maior_de_idade(),self.data_nascimento)