class Funcionario:
    def __init__(self,nome,cargo,salario):
        self.nome = nome
        self.cargo = cargo
        self._salario = salario
    def descricao(self):
        return f"Nome: {self.nome}\nCargo:{self.cargo}\nSalario: R${self.salario:.2f}"
    def update_salario(self):
        pass
    

class Gerente:
    def __init__(self,nome,cargo,salario) -> None:
        super().__init__(nome,cargo, salario)
        self.salario = salario 
        print(f"O salário de {self.nome} é {self.new_salario}")
    def update_salario(self):
        return "3000"
    def descricao(self):
        return super().descricao() + f"Salário: {self.update_salario}"
    

f1 = Funcionario("Joao", "Assistente", 1412)
g1 = Gerente("bernardo", "Gerente", salario)
    