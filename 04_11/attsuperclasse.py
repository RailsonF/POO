from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.marca = marca 
        self.modelo = modelo
        self.ano = ano
    def descricao(self):
        return f"Ano:{self.ano} - Marca:{self.marca} - Modelo:{self.modelo}:"
    @abstractmethod
    def tipo_combustivel(self):
        pass
        
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, qtd_portas):
        super().__init__(marca, modelo, ano) 
        self.qtd_portas = qtd_portas
    def tipo_combustivel(self):
        return "Gasolina"
    def descricao(self):
        return super().descricao() + f" - N° de portas:{self.qtd_portas} - Tipo de combustível:{self.tipo_combustivel()}"

class Moto(Veiculo):
    def __init__(self,marca,modelo,ano,cilindrada):
        super().__init__(marca,modelo,ano)
        self.cilindrada = cilindrada
    def tipo_combustivel(self):
        return "Gasolina"
    def descricao(self):
        return super().descricao() + f" - Cilindrada:{self.cilindrada} - Tipo de combustível:{self.tipo_combustivel()}"

class Caminhao(Veiculo):
    def __init__(self,marca,modelo,ano,carga_max):
        super().__init__(marca,modelo,ano)
        self.carga_max = carga_max
    def tipo_combustivel(self):
        return "Diesel"
    def descricao(self):
       return super().descricao() + f" - Carga Máx:{self.carga_max} Toneladas - Tipo de combustível:{self.tipo_combustivel()}"
    
def mostrar_informacoes(objetos):
    print(objetos.descricao())
celta = Carro("chevrolet", "Celta", 2012, 2)
hornet = Moto("Honda", "Hornet",2014, 600)
mercedes = Caminhao("Mercedes","Carreta", 2010, 2)

mostrar_informacoes(celta)
mostrar_informacoes(hornet)
mostrar_informacoes(mercedes)
