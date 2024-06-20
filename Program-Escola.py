# Importa a biblioteca mysql.connector para conectar e interagir com um banco de dados MySQL.
import mysql.connector

# Define a classe Aluno com atributos relacionados a um aluno.
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome  # Inicializa o atributo nome.
        self.idade = idade  # Inicializa o atributo idade.

# Define a classe Professor com atributos relacionados a um professor.
class Professor:
    def __init__(self, nome, materia):
        self.nome = nome  # Inicializa o atributo nome.
        self.materia = materia  # Inicializa o atributo materia.

# Define a classe Curso com atributos relacionados a um curso.
class Curso:
    def __init__(self, nome, carga_horaria):
        self.nome = nome  # Inicializa o atributo nome.
        self.carga_horaria = carga_horaria  # Inicializa o atributo carga_horaria.

# Define a classe SistemaEscola que gerencia a conexão com o banco de dados e as operações CRUD.
class SistemaEscola:
    def __init__(self):
        # Inicializa a conexão com o banco de dados MySQL.
        self.conexao = mysql.connector.connect(
            host='localhost',  # Endereço do servidor de banco de dados.
            user='root',  # Nome de usuário para a conexão.
            password='he182555@',  # Senha do usuário.
            database='escola'  # Nome do banco de dados a ser utilizado.
        )
        self.cursor = self.conexao.cursor()  # Cria um cursor para executar comandos SQL.

    # Método para adicionar um aluno no banco de dados.
    def adicionar_aluno(self, aluno):
        sql = 'INSERT INTO aluno (nome_aluno, idade_aluno) VALUES (%s, %s)'  # Comando SQL para inserir um novo aluno.
        valores = (aluno.nome, aluno.idade)  # Tupla com os valores a serem inseridos.
        self.cursor.execute(sql, valores)  # Executa o comando SQL com os valores fornecidos.
        self.conexao.commit()  # Confirma a transação no banco de dados.
        print('Aluno adicionado com sucesso.')  # Imprime uma mensagem de sucesso.

    # Método para adicionar um professor no banco de dados.
    def adicionar_professor(self, professor):
        sql = 'INSERT INTO professor (nome_professor, materia_professor) VALUES (%s, %s)'  # Comando SQL para inserir um novo professor.
        valores = (professor.nome, professor.materia)  # Tupla com os valores a serem inseridos.
        self.cursor.execute(sql, valores)  # Executa o comando SQL com os valores fornecidos.
        self.conexao.commit()  # Confirma a transação no banco de dados.
        print('Professor adicionado com sucesso.')  # Imprime uma mensagem de sucesso.

    # Método para adicionar um curso no banco de dados.
    def adicionar_curso(self, curso):
        sql = 'INSERT INTO curso (nome_curso, carga_horaria) VALUES (%s, %s)'  # Comando SQL para inserir um novo curso.
        valores = (curso.nome, curso.carga_horaria)  # Tupla com os valores a serem inseridos.
        self.cursor.execute(sql, valores)  # Executa o comando SQL com os valores fornecidos.
        self.conexao.commit()  # Confirma a transação no banco de dados.
        print('Curso adicionado com sucesso.')  # Imprime uma mensagem de sucesso.

    # Método para listar todos os alunos do banco de dados.
    def listar_alunos(self):
        self.cursor.execute('SELECT nome_aluno, idade_aluno FROM aluno')  # Comando SQL para selecionar nome_aluno e idade_aluno dos alunos.
        alunos = self.cursor.fetchall()  # Recupera todos os resultados da consulta.
        for aluno in alunos:  # Itera sobre cada aluno recuperado.
            print(f'Nome: {aluno[0]}, Idade: {aluno[1]}')  # Imprime os detalhes de cada aluno.

    # Método para listar todos os professores do banco de dados.
    def listar_professores(self):
        self.cursor.execute('SELECT nome_professor, materia_professor FROM professor')  # Comando SQL para selecionar nome_professor e materia_professor dos professores.
        professores = self.cursor.fetchall()  # Recupera todos os resultados da consulta.
        for professor in professores:  # Itera sobre cada professor recuperado.
            print(f'Nome: {professor[0]}, Matéria: {professor[1]}')  # Imprime os detalhes de cada professor.

    # Método para listar todos os cursos do banco de dados.
    def listar_cursos(self):
        self.cursor.execute('SELECT nome_curso, carga_horaria FROM curso')  # Comando SQL para selecionar nome_curso e carga_horaria dos cursos.
        cursos = self.cursor.fetchall()  # Recupera todos os resultados da consulta.
        for curso in cursos:  # Itera sobre cada curso recuperado.
            print(f'Nome do Curso: {curso[0]}, Carga Horária: {curso[1]} horas')  # Imprime os detalhes de cada curso.

    # Método para fechar a conexão com o banco de dados.
    def fechar_conexao(self):
        self.cursor.close()  # Fecha o cursor.
        self.conexao.close()  # Fecha a conexão com o banco de dados.
        print("Conexão ao banco de dados fechada.")  # Informa que a conexão foi fechada com sucesso.

# Função para exibir o menu e obter a escolha do usuário.
def menu():
    print("Sistema de Gerenciamento Escolar")
    print("1. Adicionar Aluno")
    print("2. Adicionar Professor")
    print("3. Adicionar Curso")
    print("4. Listar Alunos")
    print("5. Listar Professores")
    print("6. Listar Cursos")
    print("7. Sair")

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente (não importado como módulo).
    sistema_escola = SistemaEscola()  # Cria uma instância do sistema de gerenciamento escolar.

    while True:  # Loop infinito para exibir o menu e lidar com as escolhas do usuário.
        menu()  # Exibe o menu para o usuário.
        opcao = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção.

        if opcao == '1':  # Se a escolha for adicionar aluno.
            nome = input("Nome do Aluno: ")  # Solicita o nome do aluno.
            idade = int(input("Idade do Aluno: "))  # Solicita a idade do aluno.
            aluno = Aluno(nome, idade)  # Cria um objeto Aluno com os dados fornecidos.
            sistema_escola.adicionar_aluno(aluno)  # Adiciona o aluno no banco de dados.

        elif opcao == '2':  # Se a escolha for adicionar professor.
            nome = input("Nome do Professor: ")  # Solicita o nome do professor.
            materia = input("Matéria do Professor: ")  # Solicita a matéria do professor.
            professor = Professor(nome, materia)  # Cria um objeto Professor com os dados fornecidos.
            sistema_escola.adicionar_professor(professor)  # Adiciona o professor no banco de dados.

        elif opcao == '3':  # Se a escolha for adicionar curso.
            nome = input("Nome do Curso: ")  # Solicita o nome do curso.
            carga_horaria = int(input("Carga Horária do Curso: "))  # Solicita a carga horária do curso.
            curso = Curso(nome, carga_horaria)  # Cria um objeto Curso com os dados fornecidos.
            sistema_escola.adicionar_curso(curso)  # Adiciona o curso no banco de dados.

        elif opcao == '4':  # Se a escolha for listar alunos.
            print("Lista de Alunos: ")
            sistema_escola.listar_alunos()  # Lista todos os alunos do banco de dados.

        elif opcao == '5':  # Se a escolha for listar professores.
            print("Lista de Professores: ")
            sistema_escola.listar_professores()  # Lista todos os professores do banco de dados.

        elif opcao == '6':  # Se a escolha for listar cursos.
            print("Lista de Cursos: ")
            sistema_escola.listar_cursos()  # Lista todos os cursos do banco de dados.

        elif opcao == '7':  # Se a escolha for sair.
            sistema_escola.fechar_conexao()  # Fecha a conexão com o banco de dados.
            print("Saindo do sistema...")  # Informa que o sistema está sendo encerrado.
            break  # Sai do loop.

        else:  # Se a escolha for inválida.
            print("Opção inválida, por favor escolha novamente.")  # Informa ao usuário que a opção é inválida.

