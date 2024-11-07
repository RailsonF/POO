class Funcionario:
    def __init__(self,nome,cargo,_salario):
        self.nome = nome
        self.cargo = cargo
        self._salario = _salario
    def descricao(self):
        return f"Nome: {self.nome}\nCargo:{self.cargo}\nSalario: R${self.salario:.2f}"
    
class Gerente:
    def __init__(self,nome,cargo,bonus,_salario = 1412):
        super().__init__(nome,cargo, _salario)
        self.bonus = bonus
        self.calcular_salario()
    def calcular_salario(self):
        self.salario += self.bonus
    def descricao(self):
        return super().descricao()
    

f1 = Funcionario("Joao", "Assistente", 1412)
g1 = Gerente("bernardo", "Gerente", 200)
g1.calcular_salario()
print(g1.descricao())
print(f1.descricao())