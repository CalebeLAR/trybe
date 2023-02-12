-- DROP SCHEMA IF EXISTS brasil;
-- CREATE SCHEMA brasil;
-- USE brasil;

-- CREATE TABLE cidades(
--   cidade VARCHAR(100) NOT NULL,
--   estado VARCHAR(10) NOT NULL,
--   populacao INTEGER,
--   CONSTRAINT PRIMARY KEY(cidade)
-- );

DROP SCHEMA IF EXISTS league_of_legends;
DROP TABLE IF EXISTS league_of_legends.personagens;
CREATE SCHEMA league_of_legends;

CREATE TABLE league_of_legends.personagens(
	nome VARCHAR(20) NOT NULL,
    classe VARCHAR(10) NOT NULL,
    poderzin_Q VARCHAR(50), 
    poderzin_W VARCHAR(50),
    poderzin_E VARCHAR(50),
    ultimate VARCHAR(50),
    CONSTRAINT PRIMARY KEY (nome)
);

USE league_of_legends;
INSERT INTO personagens
	(nome, classe, poderzin_Q, poderzin_W, poderzin_E, ultimate )
VALUE
	('jhin', 'atirador', 'dano que quika', 'raio que estuna', 'bombinha invisivel', 'quatro tiro gigante');









