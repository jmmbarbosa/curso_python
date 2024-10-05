class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def get_salario(self):
        print("Meu salário é: ", self.salario)

    def get_bonificacao(self):
        return self.salario * 0.15
    
jose = Funcionario("José Milton", "575.899.955-25", 7000)
jose.get_salario()
print(jose.get_bonificacao())
