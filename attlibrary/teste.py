class Pessoa:
    def __init__(self, nome, idade, _num_matricula):
        self.nome = nome
        self.idade = idade
        self._num_matricula = _num_matricula
    #def __str__(self):   
        #return f"Usuário {self.nome} cadastrado com sucesso!!"
class Livro:
    def __init__(self, titulo, autor, ano_publi, status_disponibilidade):
        self.titulo = []
        self.autor = autor
        self.ano_publi = ano_publi
        self.status_disponibilidade = status_disponibilidade

class UsuarioComum(Pessoa, Livro):
    def __init__(self, nome, idade, _num_matricula, lendo_livro):
        super().__init__(nome, idade, _num_matricula)
        self.nome = nome
        self.idade = idade
        self._num_matricula = _num_matricula
        self.lendo_livro = []
        
    
    
class Adm(Pessoa, Livro):
    def __init__(self, nome, idade, _num_matricula,_senha):
        super().__init__(nome, idade, _num_matricula)
        self._senha = _senha
          
    #def __str__(self):
     #   return super().__str__() + f"a senha do ADM é{self._senha}:"
      
    
    def cadastrar_livro(self, titulo, autor, ano_publi, status_disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.ano_publi = ano_publi
        self.status_disponibilidade = status_disponibilidade
        return f"Livro {self.titulo} cadastrado com sucesso!!"
    def cadastrar_users(self,nome, idade, _num_matricula):
        self.nome = nome
        self.idade = idade
        self._num_matricula = _num_matricula
        return f"usuário {self.nome} cadastrado com sucesso!!"
    def cad_emprestimo(self, nome, titulo):
        self.nome = nome
        self.titulo = titulo
        return f"Livro: {self.nome} emprestado para o usuário {self.titulo}"
    
        
        


adm1 = Adm("Railson",19, 102552, 123456)
cad_li1 = adm1.cadastrar_livro("O senhor dos anéis", "J. R. R. Tolkien",1954, "livre")
cad_user1 = adm1.cadastrar_users("Wellington", 35, 102655)
cad_empres1 = adm1.cad_emprestimo("Wellington", "O senhor dos anéis")
print(cad_li1,"\n", cad_user1, "\n", cad_empres1)

#l1 = Livro("O senhor dos anéis", "J. R. R. Tolkien",1954, "livre")
#print(l1)
