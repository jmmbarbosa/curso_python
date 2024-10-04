class Veiculo():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindrada = cilindrada

class Aviao():
    def __init__(self, tipo, motor, linha_aerea, modelo, ano):
        self.tipo = tipo
        self.motor = motor
        self.linha_aerea = linha_aerea
        self.modelo = modelo
        self.ano = ano

carro = Veiculo('carro', '84GFHKK9879796KK89L', 'MARCAX', 'X001', '2020')
print(vars(carro))
moto = Motocicleta('motocicleta', 'MH67658EL1234587ML', 'Honda', 'Elite 125', '2020', 125)
print(vars(moto))
objeto_aviao = Aviao('CARGA', 'QUADRIMOTO', '1000TON AIRLINES', 'AIRBUS M300', '2010')
print(vars(objeto_aviao))
