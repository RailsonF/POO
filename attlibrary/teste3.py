class Pessoa:
    def __init__(self, nome, idade, _num_matricula):
        self.nome = nome
        self.idade = idade
        self._num_matricula = _num_matricula
    def __str__(self):
        return f"Usuário{self.nome} cadastrado com sucesso"
class Livro:
    def __init__(self, titulo, autor, ano_publi, status_disponibilidade = "disponivel"):
        self.titulo = titulo
        self.autor = autor
        self.ano_publi = ano_publi
        self.status_disponibilidade = status_disponibilidade
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publi}"

class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, _num_matricula):
        super().__init__(nome, idade, _num_matricula)
        self.livros_emprestados = []
    def __str__(self):
        return super().__str__()


    def emprestimo(self,livro):
        if livro.status_disponibilidade == "disponivel":
            livro.status_disponibilidade = "Emprestado"
            self.livros_emprestados.append(livro)
            return f"Livro {livro.titulo} emprestado para {self.nome}"
            return f"Livro: {self.titulo} emprestado para o usuário {self.nome}"
        else:
            return f"Livro não disponível para empréstimo"
        
class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self,livro):
        self.livros.append(livro)
    

class Adm(Pessoa):
    def __init__(self, nome, idade, _num_matricula,_senha):
        super().__init__(nome, idade, _num_matricula)
        self._senha = _senha
    def __str__(self):
        return super().__str__()
      
    #Método que vai cadastrar um livro
    def cadastrar_livro(self, titulo, autor, ano_publi, status_disponibilidade):
        novo_livro = Livro(titulo,autor,ano_publi,status_disponibilidade)
        biblioteca.adicionar_livro(novo_livro)
        return novo_livro
    
        ''''
        self.titulo = titulo
        self.autor = autor
        self.ano_publi = ano_publi
        self.status_disponibilidade = status_disponibilidade
        return f"Livro {self.titulo} cadastrado com sucesso!!"
        '''
#Criando a instancia de biblioteca
biblioteca = Biblioteca()

#Instanciando o objeto da classe ADM
adm1 = Adm("Railson",19, 102552, 123456)

#Caastrando livro e usuário
livro1 = adm1.cadastrar_livro(biblioteca,"O senhor dos anéis", "J. R. R. Tolkien",1954)
usuario1= UsuarioComum("ze", 12547, 579)
emprestimo1 = usuario1.emprestimo(livro1)
print(livro1,"\n",usuario1, "\n", emprestimo1)
