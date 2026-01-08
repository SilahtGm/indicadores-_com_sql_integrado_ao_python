# Importando bibliotecas
import sqlite3
import os


# Função principal de criação/conexão de banco de dados
def inicializar_banco():
    try:
        # Guardando na variavel a checagem de se o banco de dados ja existe
        banco_existe = os.path.exists('database.db')

        # Guardando na variavel conexao a conexao do sqlite3, e fazendo a conexao
        # com o banco de dados localizado no arquivp database.db, se ele não existir
        # vai ser criado agora
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        # 1. Tenta abrir e rodar o Schema, guardadp no arquivo schema.sql
        with open('schema.sql', 'r', encoding='utf-8') as f:
            cursor.executescript(f.read())

        # 2. Tenta abrir e rodar os Inserts apenas se o banco for novo
        if not banco_existe:
            with open('inserts.sql', 'r', encoding='utf-8') as g:
                cursor.executescript(g.read())
            print(">>> Sucesso: Banco criado e populado pela primeira vez.")
        else:
            print(">>> Conectado: Banco de dados já existente.")

        conexao.commit()
        conexao.close()

    except FileNotFoundError as e:
        print(f"Erro: Arquivo de script não encontrado! Detalhes: {e}")
    except sqlite3.Error as e:
        print(f"Erro no Banco de Dados (SQLite): {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")



# Funções Principais
def login():
    print("\n>> Área de Login")
    email = input("Email: ")
    senha = input("Senha: ")

def criar_conta():
    print("\n>> Criar Nova Conta")
    nome = input("Seu nome: ")
    email = input("Seu email: ")
    senha = input("Crie uma senha: ")

def encerrando():
    print("\nEncerrando o sistema. Até mais!")



# Funções Menu


def menu():
    while True:
        print("\n=============================")
        print(" Sistema de Gestão Financeira ")
        print("=============================")
        print(" 1 - Fazer Login")
        print(" 2 - Criar Nova Conta")
        print(" 0 - Sair do Sistema")
        print("=============================")
        op = input("Escolha uma opção: ")

        match op:

            case "1":
                login()
            case "2":
                criar_conta()
            case "0":
                encerrando()
            case _:
                print("\n[!] Opção inválida. Tente novamente.")
                break



def menu_pos_login(nome_usuario, id_usuario):
    while True:
        print(f"\n=============================")
        print(f"   PAINEL: {nome_usuario.upper()} ")
        print("=============================")
        print(" 1 - Ver Saldo Atual")
        print(" 2 - Registrar Transação (Gasto/Ganho)")
        print(" 3 - Extrato Detalhado")
        print(" 4 - Relatório Gráfico (Matplotlib)")
        print(" 5 - Gerenciar Metas")
        print(" 0 - Logout (Sair)")
        print("=============================")

        opcao = input("Escolha uma operação: ")

        match opcao:
            case "1":
                print(f"\n[Consultando saldo do usuário {id_usuario}...]")
                # chamar_funcao_saldo(id_usuario)

            case "2":
                print("\n[Nova Transação]")
                # chamar_funcao_registro(id_usuario)

            case "3":
                print("\n[Gerando extrato...]")
                # chamar_funcao_extrato(id_usuario)

            case "4":
                print("\n[Abrindo visualização gráfica...]")
                # chamar_funcao_grafico(id_usuario)

            case "5":
                print("\n[Metas Econômicas]")
                # chamar_funcao_metas(id_usuario)

            case "0":
                print(f"\nSaindo da conta de {nome_usuario}...")
                break # Volta para o menu de login

            case _:
                print("\n[!] Opção incorreta. Escolha entre 0 e 5.")


