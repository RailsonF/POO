'''
class Aluno:
    def __init__(self, nota):
        self.nota = nota
        print(f"{self.nome} recebeu a nota {self.nota}")
class professor:
    def __init__(self, nome):
        self.nome = None
    def atribuir_nota(self, nota):
'''
'''
class Pessoa:
    def __init__(self, nome, livro_nome):
        self.nome = nome
        self.livro_nome = None
    def lendo(self):
        print(f"{self.nome} está lendo o livro {self.livro_nome}")

class Livro:
    def __init__(self,livro_nome, nome):
        self.livro_nome = livro_nome
        self.nome = None
      
    def lido(self):
        print(f"O livro {self.livro_nome} foi lido por {self.nome}")



p1 = Pessoa("Wellington")
liv = Livro("O senhor dos anéis")
p1.lendo()
liv.lido()
'''
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.livro_nome = None
    def lendo(self):
            print(f"{self.nome} está lendo o livro {self.livro_nome}")

class Livro:
    def __init__(self,livro_nome):
        self.livro_nome = livro_nome
        self.nome = None
      
    def lido(self):
        print(f"O livro {self.livro_nome} foi lido por {self.nome}")


p1 = Pessoa("Wellington")
liv = Livro("O senhor dos anéis")
p1.lendo()
liv.lido()