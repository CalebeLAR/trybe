-- Chave primária composta
DROP SCHEMA IF EXISTS brasil;

CREATE DATABASE brasil;
USE brasil;
CREATE TABLE cidades (
  `cidade` VARCHAR(100) NOT NULL,
  `estado` VARCHAR(10) NOT NULL,
  `populacao` INTEGER,
  CONSTRAINT PRIMARY KEY(cidade)
);

  -- Apagar a versão antiga da tabela
  DROP TABLE cidades;

  -- Cria uma tabela
  CREATE TABLE cidades(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  cidade VARCHAR(100) NOT NULL,
  estado VARCHAR(10) NOT NULL,
  populacao INTEGER
  );

  -- Insere os dados na tabela
  INSERT INTO cidades(cidade, estado, populacao)
  VALUES('Rio Claro','SP',185421),
  ('Rio Claro','RJ',17216);

-- não funciona a menos se colocarmos uma segunda coluna como primary key
INSERT INTO cidades (cidade, estado, populacao)
VALUES("Rio Claro","SP",185421), ("Rio Claro","RJ",17216);