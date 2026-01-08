# Importando bibliotecas
import sqlite3 #sqlite para banco de dados
import os #os para informações do sistema



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

        # 2. Tenta abrir e rodar os Inserts apenas se o banco for novo, caso
        # contrario, apenas exibira que estará estabelecendo a conexão, os inserts
        # armazenado em inserts.sql
        if not banco_existe:
            with open('inserts.sql', 'r', encoding='utf-8') as g:
                cursor.executescript(g.read())
            print(">>> Sucesso: Banco criado e populado pela primeira vez.")
        else:
            print(">>> Conectado: Banco de dados já existente.")

        # Salvando e fechando a conexão
        conexao.commit()
        conexao.close()

    # Excepts trazendo possiveis mensagens de erro
    except FileNotFoundError as e:
        print(f"Erro: Arquivo de script não encontrado! Detalhes: {e}")
    except sqlite3.Error as e:
        print(f"Erro no Banco de Dados (SQLite): {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")



# Funções Principais
def login():
        print("\n======================================")
        print("      ÁREA DE ACESSO")
        print("\n======================================")

        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")

        # Conecta ao banco de dados
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Busca o usuário com esse email e essa senha
        query = "SELECT id_usuario, nm_usuario FROM usuarios WHERE email = ? AND senha = ?"
        cursor.execute(query, (email, senha))

        usuario = cursor.fetchone()  # Tenta pegar uma linha
        conn.close()

        if usuario:
            # Se encontrou, usuario[0] é o ID e usuario[1] é o Nome
            print(f"\n[+] Bem-vindo de volta, {usuario[1]}!")
            menu_pos_login(usuario)
            return usuario  # Retorna (id, nome) para usar no sistema

        else:
            print("\n[!] E-mail ou senha incorretos.")
            return None

def criar_conta():
    print("\n======================================")
    print("      CRIAÇÃO DE CONTA")
    print("======================================")
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # 1. Executa a inserção
        query = "INSERT INTO usuarios (nm_usuario, email, senha) VALUES (?, ?, ?);"
        cursor.execute(query, (nome, email, senha))

        # 2. IMPORTANTE: Salva a alteração no banco de dados
        conn.commit()

        # 3. Verifica se o ID foi gerado (confirmação de sucesso)
        if cursor.lastrowid:
            print("\n[+] Conta criada com sucesso!")
            print("[+] Acesse na área de Login")
        else:
            print("\n[!] Ocorreu um erro na criação da sua conta.")
        conn.close()
    except sqlite3.IntegrityError:
        print("\n[!] Erro: Este e-mail já está cadastrado!")
    except sqlite3.Error as e:
        print(f"\n[!] Erro no Banco de Dados (SQLite): {e}")
    except Exception as e:
        print(f"\n[!] Erro inesperado: {e}")




def encerrando():
    print("\nEncerrando o sistema. Até mais!")

# Funções secundarias

def checar_saldo(usuario):
    id_usuario = usuario[0]
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        tipo = "Entrada"
        query1 = "SELECT SUM(valor) FROM transacoes WHERE id_usuario = ? AND tipo = ?"
        cursor.execute(query1, (id_usuario, tipo))
        entrada = cursor.fetchone()

        tipo2 = "Saída"
        query2 = "SELECT SUM(valor) FROM transacoes WHERE id_usuario = ? AND tipo = ?"
        cursor.execute(query2,(id_usuario, tipo2))
        saida = cursor.fetchone()

        saldo = entrada[0] - saida[0]

        print(f"\n=============================")
        print(f"   SALDO ATUAL: R$ {saldo}")
        print(f"   (Entradas: R$ {entrada} | Saídas: R$ {saida})")
        print(f"=============================")

        conn.commit()
        conn.close()


    except sqlite3.Error as e:
        print(f"\n[!] Erro no Banco de Dados: {e}")




def registrar_transacao(usuario):
    id_usuario = usuario[0]

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()


        while True:
            print("====================================")
            print("  NOVO REGISTRO")
            print("====================================")
            tipo = input("Tipo (1 - ENTRADA / 2 - SAÍDA / 0 - VOLTAR): ")

            if tipo == "0":
                break

            id_categoria = None

            if tipo == "1":
                tipo_db = "Entrada"
                print("\nCategorias de RECEITA:")
                op = input("1 - SALÁRIO / 2 - INVESTIMENTO: ")
                match op:
                    case "1":
                        id_categoria = 3
                    case "2":
                        id_categoria = 4
                    case _:
                        print("[!] Opção inválida."); continue

            elif tipo == "2":
                tipo_db = "Saída"
                print("\nCategorias de DESPESA:")
                op = input("1 - ALIMENTAÇÃO / 2 - LAZER / 3 - EDUCAÇÃO / 4 - TRANSPORTE: ")
                match op:
                    case "1":
                        id_categoria = 1
                    case "2":
                        id_categoria = 2
                    case "3":
                        id_categoria = 5
                    case "4":
                        id_categoria = 6
                    case _:
                        print("[!] Opção inválida."); continue
            else:
                print("[!] Tipo inválido.")
                continue

            # Se chegamos aqui, os tipos estão certos
            try:
                valor = float(input("Valor: R$ "))
                descricao = input("Descrição: ")

                from datetime import date
                data_hoje = date.today().isoformat()

                # 3. INSERT (Incluindo a coluna 'tipo' para facilitar seu saldo depois)
                query = """
                    INSERT INTO transacoes (id_usuario, id_categoria, valor, tipo, data, descricao) 
                    VALUES (?, ?, ?, ?, ?, ?)
                """
                cursor.execute(query, (id_usuario, id_categoria, valor, tipo_db, data_hoje, descricao))
                conn.commit()
                print("\n[+] Transação registrada com sucesso!")

                # Pergunta se quer continuar
                continuar = input("\nDeseja registrar outra? (S/N): ").upper()
                if continuar != 'S':
                    break
                conn.close()

            except ValueError:
                print("\n[!] Erro: Use apenas números e ponto para o valor.")

    except sqlite3.Error as e:
        print(f"\n[!] Erro no Banco de Dados: {e}")



# Funções Menu


def menu():
    inicializar_banco()
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


def menu_pos_login(usuario):
    id_usuario = usuario[0]
    nm_usuario = usuario[1]

    while True:
        print(f"\n==========================================")
        print(f"       SGF - PAINEL DE CONTROLE           ")
        print(f"       Usuário: {nm_usuario.upper()}")
        print(f"==========================================")
        print(" [1] VISÃO GERAL (Saldo)")
        print(" [2] REGISTRAR ENTRADA/SAÍDA")
        print(" [3] RELATÓRIOS E GRÁFICOS (Matplotlib)")
        print(" [4] PLANEJAMENTO (Metas Econômicas)")
        print(" [5] CONFIGURAÇÕES (Categorias)")
        print(" [0] LOGOUT")
        print("==========================================")

        opcao = input("Escolha uma operação: ")

        match opcao:
            case "1":
                checar_saldo(usuario)


            case "2":
               registrar_transacao(usuario)


            case "3":
                # Aqui entra o Pandas e Matplotlib
                # gerar_grafico_gastos(id_usuario)
                print("Em desenvolvimento...")
            case "4":
                # Operações com a tabela 'metas_economicas'
                # menu_metas(id_usuario)
                print("Em desenvolvimento...")

            case "5":
                # O usuário pode querer ver ou adicionar novas categorias
                # visualizar_categorias()
                print("Em desenvolvimento...")


            case "0":
                print(f"\nEncerrando sessão de {nm_usuario}...")
                break

            case _:
                print("\n[!] Opção incorreta. Tente novamente.")


# APOIO DE ESTUDOS
# ==============================================================================
# GUIA DE MÉTODOS DO CURSOR (SQLITE3)
# ==============================================================================

# cursor.execute(query, params)
# -> O MAIS USADO: Envia um comando SQL para o banco de dados.
# -> Use '?' como placeholder para passar variáveis com segurança.
# Ex: cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_user,))

# cursor.fetchone()
# -> BUSCA UMA LINHA: Retorna a primeira linha do resultado da consulta.
# -> Útil para: Logins, somas de saldo (SUM) ou buscar um item específico.
# -> Retorna: Uma TUPLA se achar algo, ou NONE se não achar nada.

# cursor.fetchall()
# -> BUSCA TUDO: Retorna uma LISTA contendo todas as linhas da consulta.
# -> Útil para: Listar extratos, mostrar todas as categorias ou metas.
# -> Retorna: Uma lista de tuplas [ (id1, nome1), (id2, nome2) ].

# cursor.lastrowid
# -> O "RG" DO NOVO REGISTRO: Retorna o ID (PK) da última linha que você inseriu.
# -> Útil para: Confirmar se o INSERT funcionou ou vincular dados na hora.
# -> Só funciona após comandos INSERT.

# cursor.executescript(string_sql)
# -> MÚLTIPLOS COMANDOS: Executa vários comandos SQL de uma vez (separados por ;).
# -> Útil para: Rodar o arquivo 'schema.sql' ou 'inserts.sql' na inicialização.

# cursor.rowcount
# -> LINHAS AFETADAS: Diz quantas linhas foram alteradas pelo último comando.
# -> Útil para: Saber se um UPDATE ou DELETE realmente alterou algo no banco.
# ==============================================================================

menu()