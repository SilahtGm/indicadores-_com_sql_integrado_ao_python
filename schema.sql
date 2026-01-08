-- Criação da tabela de Usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nm_usuario TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela de Categorias
CREATE TABLE IF NOT EXISTS categorias (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nm_categoria TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('Receita', 'Despesa')) -- Garante apenas esses dois valores
);

-- Criação da tabela de Transações
CREATE TABLE IF NOT EXISTS transacoes (
    id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,
    valor REAL NOT NULL,
    tipo TEXT CHECK(tipo IN ('Entrada', 'Saída')),
    data DATE NOT NULL,
    descricao TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
    FOREIGN KEY (id_categoria) REFERENCES categorias (id_categoria)
);

-- Criação da tabela de Metas Econômicas
CREATE TABLE IF NOT EXISTS metas_economicas (
    id_metas INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    valor_objetivo REAL NOT NULL,
    objetivo TEXT,
    prazo DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
);