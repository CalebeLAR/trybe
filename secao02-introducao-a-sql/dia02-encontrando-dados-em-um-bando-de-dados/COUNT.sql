-- Sobre a tabela staff do banco de dados sakila. 

-- Quantas senhas temos cadastradas nessa tabela?
SELECT COUNT(password) FROM sakila.staff;
-- Quantas pessoas temos no total trabalhando para nossa empresa?
SELECT COUNT(*) FROM sakila.staff;