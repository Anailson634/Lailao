import json
from random import randint, choice as ch

class Carro:
    def __init__(self):
        self.db_carros={}
        self.list_names=[]
        self.list_cor=['red', 'blue', 'white', 'black']
        self.alfabeto=['D', "LK", 'I', 'RE', 'L', 'GA',
                            'UD', 'E', 'QL', 'M', 'ZF', 'B']
        self.numero=['34', '6', '89', '3', '04', '9',
                            '7', '17', '5', '32', '7', '00']
        
        self.carro_name=None
        self._path=None
        
        self.preco=0
        self.desvalor=0
        self.nivel=None
        self.reparar=0 #Indefinido

        self.placa=ch(self.alfabeto),ch(self.alfabeto),ch(self.numero),ch(self.numero)

        self.motor_cc=None
        self.estado_motor=randint(0, 100)
        self.reparo_motor=0

        self.cor=ch(self.list_cor)
        self.estado_lataria=randint(0, 100)
        self.reparo_lataria=0

        with open("python/carros.json", 'r', encoding="utf8") as arq:
            self.db_carros=json.load(arq)

    def criar_caracteristicas(self):
        self.list_names=list(self.db_carros.keys()) #Adiciona os nomes dos carros a self.list_names
            
        self.carro_name=ch(self.list_names) #Escolhe o carro
        self._path=self.db_carros[self.carro_name]["_path"]
        motor=list(self.db_carros[self.carro_name]["spect"].keys()) #Pega informações do carro escolhido
            
        self.motor_cc=ch(motor) #Seleciona o motor
        self.preco=self.db_carros[self.carro_name]["spect"][self.motor_cc] #preço na tabela fipe (Ou novo)

    def danos_motor(self):
        """Quanto mais danificado mais desvalorizado vai ser o valor final (self.preco_final)
        Podendo ganar um aumento de valor ao reparar o carro"""
        num_motor=float(self.motor_cc[:3].replace("V", ""))

        if num_motor > 100:
            self.reparo_motor=self.estado_motor*15
        elif num_motor >= 1.0 and num_motor <= 1.3:
            self.reparo_motor=self.estado_motor*25
        elif num_motor >= 1.4 and num_motor <=1.6:
            self.reparo_motor=self.estado_motor*35
        else:
            self.reparo_motor=self.estado_motor*45
        
        self.reparar=self.reparo_lataria+self.reparo_motor
        self.desvalor=0.46*self.reparar
        self.preco=(self.preco-(self.desvalor))-self.reparar #Valor final

    def danos_lataria(self):
        if self.preco >1000 and self.preco <= 16000:
            self.reparo_lataria=self.estado_lataria*20
        elif self.preco >16000 and self.preco <= 25000:
            self.reparo_lataria=self.estado_lataria*35
        elif self.preco >25000 and self.preco <= 56000:
            self.reparo_lataria=self.estado_lataria*60
        elif self.preco >56000 and self.preco <= 85000:
            self.reparo_lataria=self.estado_lataria*80


def gerar_lista(quantidade):
    list_cars={}

    for c in range(0, quantidade):
        _carro=Carro()
        _carro.criar_caracteristicas()
        _carro.danos_lataria()
        _carro.danos_motor()

        list_cars[_carro.carro_name]={
        "Cor": _carro.cor,
        "Lataria": _carro.estado_lataria,
        "Lat_rs": _carro.reparo_lataria,
        "Motor": _carro.estado_motor,
        "Mot_rs": _carro.reparo_motor,
        "Placa": _carro.placa,
        "Motor-cc":_carro.motor_cc,
        "Reparo": _carro.reparar,
        "Desvalorizacao": _carro.desvalor,
        "Preço_final": _carro.preco,
        "preço_original": _carro.db_carros[_carro.carro_name]["spect"][_carro.motor_cc],
        "_path": _carro._path}
    return list_cars

if __name__=="__main__":
    for k,v in gerar_lista(2).items():
        print(k)
        for r, t in v.items():
            print(f"\t{r}: {t}")
