@rob4tiO
@rob4 SQL 14
hutdown -s -f -t 3600
https://www.youtube.com/watch?v=XnWaZEmIO4k&ab_channel=UskoKruM2010

---- Teste 3 - Banco de dados -----
Neste teste o candidato deverá criar scripts .sql
 (MySQL 8. ou Postgres >10.0) que execute as tarefas de código abaixo.*

Tarefas de Preparação (podem ser feitas manualmente):

* Baixar os arquivos dos últimos 2 anos no repositório público: 
http://ftp.dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/

Baixar csv anexo:

* Relatorio_cadop(1) (esta em anexo no e-mail)

As tarefas abaixo devem ser executadas em código na linguagem SQL em um banco PostgreSQL ou MySQL

Criar queries para criar tabelas com as colunas necessárias para o arquivo csv.

Queries de load: criar as queries para carregar o conteúdo dos arquivos obtidos nas tarefas de preparação
Atenção ao encoding dos arquivos no momento da importação!

Montar uma query analítica que traga a resposta para as seguintes perguntas:

Quais as 10 operadoras que mais tiveram despesas com 
SOMA VALOR FINAL da tabela 
tabela REG ANS JUNTA - 
"EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?


Junta Inner Join
SELEC reg_ans, descricao
FROM trimes2021_1
	[INNER] JOIN trimes2021_2
		ON trimes2021_1.descricao=trimes2021_2.descricao
WHERE descricao='Glosas';

filtrar 

SELEC descricao
FROM trimes2021_1, trimes2021_2, trimes2021_3
WHERE descrição = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
ORDER BY VALOR1, VALOR2,
LIMIT 10;


	Quais as 10 operadoras que mais tiveram despesas com
	"EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?


CREATE TABLE clientes (
	cod_cliente INT PRIMARY KEY,
	nome_cliente VARCHAR(20) NOT NULL,
	sobrenome_cliente VARCHAR(40) NOT NULL
);

CREATE TABLE produto (
	cod_produto INT PRIMARY KEY,
	nome_produto VARCHAR(30) NOT NULL,
	descricao TEXT NULL,
	preco NUMERIC CHECK(preco >0) NOT NULL,
	qtde_estoque SMALLINT DEFAULT 0
);

SERIAL - gera altomaticamente numero
REFERENCES - vincula a outra tabela  (chave estrangeira)

CREATE TABLE pedidos (
	cod_pedido SERIAL PRIMARY KEY,
	cod_cliente INT NOT NULL REFERENCES clientes(cod_cliente),
	cod_produto INT NOT NULL,
	qtde SMALLINT NOT NULL,
	FOREIGN KEY (cod_produto) REFERENCES produtos(cod_produto)
);
==============================================================
"DATA";"REG_ANS";"CD_CONTA_CONTABIL";"DESCRICAO";"VL_SALDO_FINAL"
CREATE TABLE trimes2021_1(
id serial primary key,
date VARCHAR(200),
reg_ans VARCHAR(200),
cd_conta_contabil VARCHAR(200),
descricao TEXT NULL,
vl_saldo VARCHAR(200)
);

"DATA";"REG_ANS";"CD_CONTA_CONTABIL";"DESCRICAO";"VL_SALDO_FINAL"

CREATE TABLE trimes2021_2(
DATA  VARCHAR(250),,
REG_ANS VARCHAR(250),
CD_CONTA_CONTABIL VARCHAR(250),
DESCRICAO TEXT NULL,
VL_SALDO_FINAL numeric(15,2)
);


nextval('trimes2021_1_id_seq'::regclass)




COPY trimes2021_1(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_final) FROM 'C:\Users\Public\localDataPostgres\1T2021.csv' DELIMITER ',' CSV HEADER;

INSERT INTO trimes2021_1 (id, data, reg_ans, cd_conta_contabil, descricao,  vl_saldo_final)
VALUES 
('0', '0', '0', '0', '0'),
('1', '1', '1', '1', '1');

SELECT * FROM trimes2021_1;

DROP TABLE trimes2021_1;

COPY trimes2021_1 FROM 'C:\Users\Public\localDataPostgres\1T2021.csv' DELIMITER ',' CSV HEADER;

======================================================

SELECT *
FROM TABELA
WHERE  COLUNA = 

======================================================

INSERT INTO clientes (cod_cliente, nome_cliente, sobrenome_cliente)
VALUES (1, 'Fabio', 'dos Reis');
INSERT INTO clientes (cod_cliente, nome_cliente, sobrenome_cliente)
VALUES (2, 'Ana', 'Teixeira');

(Consulta simples exibe tabela)
SELECT * FROM clientes;

INSERT INTO produto (cod_produto, nome_produto, descricao, preco, qtde_estoque)
VALUES
(1, 'Alcool', 'bla bla bla bla bla bla 1L', 12.99, 20),
(2, 'Luva', 'kakakak kakak akka ka 2Und', 32.20, 30),
(3, 'Sabonete', 'Huhuhuhuhuhu  HUHUhu 2Und', 22.20, 30),
(4, 'Dipirona', 'kakakak kakak akka ka 1Und', 82.20, 5); 

INSERT INTO pedidos (cod_cliente, cod_produto, qtde)
VALUES
(1, 2, 3),
(2, 3, 2),
(1, 3, 4);



CREATE DATABASE newdb;
CREATE ROLE db_user WITH LOGIN NOSUPERUSER INHERIT
 CREATEDB NOCREATEROLE NOREPLICATION PASSWORD 'StrongPassword!';
GRANT CONNECT ON DATABASE newdb TO db_user;



====== Python + SQL coneection ====
cria ambiente virtual CMD

pip install virtualenv
virtualenv myenv

myenv\Scripts\activate ou deactivate

pip list 

pip install psycopg2

pip list





