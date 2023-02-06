-- CREATE DATABASE `Escola`;
-- CREATE TABLE IF NOT EXISTS Escola.Estudantes (
--     `Nome` VARCHAR(7) CHARACTER SET utf8,
--     `Idade` INT
-- );
-- INSERT INTO Escola.Estudantes VALUES
--     ('Rafael', 25),
--     ('Amanda', 30),
--     ('Roberto', 45),
--     ('Carol', 19),
--     ('Amanda', 25);

-- Monte uma query para encontrar pares únicos de nomes e idades.
SELECT Nome, Idade FROM Escola.Estudantes;

-- Quantas linhas você encontraria na query anterior?
-- R: 5 linhas

-- Monte uma query para encontrar somente os nomes únicos.
SELECT DISTINCT Nome FROM Escola.Estudantes;

-- Quantas linhas você encontraria na query anterior?
-- R: 4 linhas

-- Monte uma query para encontrar somente as idades únicas.
SELECT DISTINCT Idade FROM Escola.Estudantes;

-- Quantas linhas você encontraria na query anterior?
-- R: 4 linhas



