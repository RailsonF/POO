class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self._salario = salario  # Tornando o salário privado (convenção)

    def descricao(self):
        return f"Nome: {self.nome}\nCargo: {self.cargo}\nSalário: R${self._salario:.2f}"

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, bonus):
        super().__init__(nome, cargo, salario)
        self._salario += bonus  # Calculando o salário total no construtor

    # Removendo o método descricao() redundante
        
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def descricao(self):
        return f"Nome: {self.nome}\nCargo: {self.cargo}\nSalário: R${self.salario:.2f}"

class Gerente(Funcionario):
    def __init__(self, nome, cargo, bonus, salario=1412):
        super().__init__(nome, cargo, salario)
        self.bonus = bonus
        self.calcular_salario()

    def calcular_salario(self):
        self.salario += self.bonus

    def descricao(self):
        return super().descricao()

f1 = Funcionario("Joao", "Assistente", 1412)
g1 = Gerente("Bernardo", "Gerente", 200)
g1.calcular_salario()  # Chamada explícita para o cálculo do salário
print(g1.descricao())