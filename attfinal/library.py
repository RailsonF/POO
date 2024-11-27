class Pessoa:
    def __init__(self, nome, idade, _num_matricula):
        self.nome = nome
        self.idade = idade
        self._num_matricula = _num_matricula

class Livro:
    def __init__(self, titulo, autor, ano_publi, status_disponibilidade="disponivel"):
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

    def emprestimo(self, livro):
        if livro.status_disponibilidade == "disponivel":
            livro.status_disponibilidade = "Emprestado"
            self.livros_emprestados.append(livro)
            return f"Livro {livro.titulo} emprestado para {self.nome}"
        else:
            return f"Livro não disponível para empréstimo"
    
    def devolucao(self,livro):
        if livro.status_disponibilidade == "Emprestado":
            livro.status_disponibilidade = "disponivel"
            self.livros_emprestados.remove(livro)
            return f"Livro {livro.titulo} devolvido por {self.nome}"
        else:
            return f"Livro disponível para empréstimo"

class Adm(Pessoa):
    def __init__(self, nome, idade, _num_matricula, _senha):
        super().__init__(nome, idade, _num_matricula)
        self._senha = _senha
        self.usuarios = []  # Lista para armazenar usuários cadastrados
        self.livros = []    # Lista para armazenar livros cadastrados

    def cadastrar_usuario(self, nome, idade, _num_matricula):
        novo_usuario = UsuarioComum(nome, idade, _num_matricula)
        self.usuarios.append(novo_usuario)
       

    def cadastrar_livro(self, titulo, autor, ano_publi, status_disponibilidade="disponivel"):
        novo_livro = Livro(titulo, autor, ano_publi, status_disponibilidade)
        self.livros.append(novo_livro)
       

    def listar_usuarios(self):
        if self.usuarios:
            print("Usuários cadastrados:")
            for usuario in self.usuarios:
                print(f"Nome: {usuario.nome}, Idade: {usuario.idade}, Matrícula: {usuario._num_matricula}")
        else:
            print("Nenhum usuário cadastrado.")

    def listar_livros(self):
        if self.livros:
            print("Livros cadastrados:")
            for livro in self.livros:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publi}, Status: {livro.status_disponibilidade}")
        else:
            print("Nenhum livro cadastrado.")


# Instanciando o administrador
adm1 = Adm("Administrador", 35, 562507, "senha1234" )

# Cadastrando usuários
adm1.cadastrar_usuario("Railson", 19, 562508)
adm1.cadastrar_usuario("Wellington", 32, 562509)

# Cadastrando livros
adm1.cadastrar_livro("O Senhor dos Anéis", "J. R. R. Tolkien", 1954)
adm1.cadastrar_livro("1984", "George Orwell", 1949)

# Listando todos os usuários e livros cadastrados
adm1.listar_usuarios()
adm1.listar_livros()

# Emprestando um livro
usuario1 = adm1.usuarios[0]  # Selecionando o primeiro usuário
livro1 = adm1.livros[0]      # Selecionando o primeiro livro
print(usuario1.emprestimo(livro1))

#Emprestando um livro2
usuario2 = adm1.usuarios[1]
livro2 = adm1.livros[1]
print(usuario2.emprestimo(livro2))

#Devolvendo um livro
print(usuario1.devolucao(livro1))
# Verificando o status dos livros após o empréstimo
adm1.listar_livros()
