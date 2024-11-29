class Pessoa:
    def __init__(self, nome, idade, _num_matricula):
        self.nome = nome
        self.idade = idade
        self._num_matricula = _num_matricula


class Livro:
    livros_cadastrados = []  # Lista de todos os livros cadastrados

    def __init__(self, titulo, autor, ano_publi, status_disponibilidade="disponivel"):
        self.titulo = titulo
        self.autor = autor
        self.ano_publi = ano_publi
        self.status_disponibilidade = status_disponibilidade


class UsuarioComum(Pessoa):
    usuarios_cadastrados = []  # Lista de todos os usuários cadastrados

    def __init__(self, nome, idade, _num_matricula):
        super().__init__(nome, idade, _num_matricula)
        self.livros_emprestados = []
    
    def emprestimo(self, livro):
        if len(self.livros_emprestados) >= 3:
            return f"{self.nome} já atingiu o limite de 3 livros emprestados."
        if livro.status_disponibilidade == "disponivel":
            livro.status_disponibilidade = "Emprestado"
            self.livros_emprestados.append(livro)
            return f"Livro {livro.titulo} emprestado para {self.nome}"
        else:
            return f"{self.nome} o livro {livro.titulo} já está emprestado"
    
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

    def cadastrar_usuario(self, nome, idade, _num_matricula):
        novo_usuario = UsuarioComum(nome, idade, _num_matricula)
        UsuarioComum.usuarios_cadastrados.append(novo_usuario)
        #return f"Usuário {nome} cadastrado com sucesso!"

    def cadastrar_livro(self, titulo, autor, ano_publi, status_disponibilidade="disponivel"):
        novo_livro = Livro(titulo, autor, ano_publi, status_disponibilidade)
        Livro.livros_cadastrados.append(novo_livro)
        #return f"Livro {titulo} cadastrado com sucesso!"

    def listar_usuarios(self):
        if UsuarioComum.usuarios_cadastrados:
            print("Usuários cadastrados:")
            for usuario in UsuarioComum.usuarios_cadastrados:
                print(f"Nome: {usuario.nome}, Idade: {usuario.idade}, Matrícula: {usuario._num_matricula}")
        else:
            print("Nenhum usuário cadastrado.")

    def listar_livros(self):
        if Livro.livros_cadastrados:
            print("Livros disponíveis:")
            for livro in Livro.livros_cadastrados:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publi}, Status: {livro.status_disponibilidade}")
        else:
            print("Nenhum livro cadastrado.")
    
    def listar_users_com_livros(self):
        print("Usuários com livros emprestados:")
        encontrou = False
        for usuario in UsuarioComum.usuarios_cadastrados:  # Corrigido para acessar a lista global de usuários
            if usuario.livros_emprestados:  # Verifica se o usuário tem livros emprestados
                encontrou = True
                print(f"Nome: {usuario.nome}, Livros:")
                for livro in usuario.livros_emprestados:
                    print(f"  - {livro.titulo}")
        if not encontrou:
            print("Nenhum usuário com livros emprestados.")

# Instanciando o administrador
adm1 = Adm("Administrador", 35, 102552, "123456")

# Cadastrando usuários
adm1.cadastrar_usuario("Railson", 19, 562508)
adm1.cadastrar_usuario("Wellington", 32, 562509)
adm1.cadastrar_usuario("Michely",19, 562510)

# Cadastrando livros
adm1.cadastrar_livro("O Senhor dos Anéis", "J. R. R. Tolkien", 1954)
adm1.cadastrar_livro("1984", "George Orwell", 1949)
adm1.cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899)
adm1.cadastrar_livro("Capitães de Areia", "Jorge Amado", 1937)
# Listando todos os usuários e livros cadastrados
adm1.listar_usuarios()
print("\n")
adm1.listar_livros()
print("\n")

# Selecionando os usuários
usuario1 = UsuarioComum.usuarios_cadastrados[0]  
usuario2 = UsuarioComum.usuarios_cadastrados[1]
usuario3 = UsuarioComum.usuarios_cadastrados[2]

# Selecionando os livros
livro1 = Livro.livros_cadastrados[0]            
livro2 = Livro.livros_cadastrados[1]
livro3 = Livro.livros_cadastrados[2]
livro4 = Livro.livros_cadastrados[3]

#Emprestando os livros aos usuários
print("\n")
print(usuario1.emprestimo(livro1))
print(usuario2.emprestimo(livro1))
print(usuario3.emprestimo(livro2))
print(usuario1.emprestimo(livro4))

#Listando os usuários com livros
adm1.listar_users_com_livros()
print("\n")
# Verificando o status dos livros após o empréstimo
adm1.listar_livros()