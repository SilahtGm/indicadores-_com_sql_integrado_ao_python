-- 1. Inserindo o Usuário Principal
INSERT INTO usuarios (nm_usuario, email, senha)
VALUES ('Thalis Sousa', 'thalis@email.com', '202020thalis');

-- 2. Populando as Categorias
INSERT INTO categorias (nm_categoria, tipo) VALUES ('Alimentação', 'Despesa');
INSERT INTO categorias (nm_categoria, tipo) VALUES ('Lazer', 'Despesa');
INSERT INTO categorias (nm_categoria, tipo) VALUES ('Salário', 'Receita');
INSERT INTO categorias (nm_categoria, tipo) VALUES ('Investimento em Ações', 'Receita');
INSERT INTO categorias (nm_categoria, tipo) VALUES ('Educação', 'Despesa');
INSERT INTO categorias (nm_categoria, tipo) VALUES ('Transporte', 'Despesa');

-- Entradas
INSERT INTO transacoes (id_usuario, id_categoria, valor, tipo, data, descricao)
VALUES (1, 3, 5000.00, 'Entrada', '2025-10-01', 'Salário Mensal');

INSERT INTO transacoes (id_usuario, id_categoria, valor, tipo, data, descricao)
VALUES (1, 4, 150.00, 'Entrada', '2025-10-15', 'Dividendos Petrobras');

-- Saídas
INSERT INTO transacoes (id_usuario, id_categoria, valor, tipo, data, descricao)
VALUES (1, 1, 120.50, 'Saída', '2025-10-02', 'Mercado Semanal');

INSERT INTO transacoes (id_usuario, id_categoria, valor, tipo, data, descricao)
VALUES (1, 5, 450.00, 'Saída', '2025-10-05', 'Curso de Python/SQL');

INSERT INTO transacoes (id_usuario, id_categoria, valor, tipo, data, descricao)
VALUES (1, 2, 80.00, 'Saída', '2025-10-10', 'Cinema e Pipoca');

INSERT INTO transacoes (id_usuario, id_categoria, valor, tipo, data, descricao)
VALUES (1, 6, 200.00, 'Saída', '2025-10-12', 'Gasolina');

-- 4. Criando uma Meta Econômica
INSERT INTO metas_economicas (id_usuario, valor_objetivo, objetivo, prazo)
VALUES (1, 10000.00, 'Reserva de Emergência', '2026-12-31');