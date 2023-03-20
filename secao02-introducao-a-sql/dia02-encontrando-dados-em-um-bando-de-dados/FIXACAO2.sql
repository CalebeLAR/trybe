-- [Para os exercícios a seguir, vamos usar a tabela sakila.actor:]
-- Escreva uma query que exiba apenas os sobrenomes únicos cadastrados.
SELECT DISTINCT(last_name) FROM sakila.actor;
-- Quantos sobrenomes únicos temos na tabela?
SELECT 
	COUNT(DISTINCT(last_name)) AS 'total de nomes unicos' ,
    COUNT(last_name) AS 'total de nomes', 
    COUNT(last_name) - COUNT(DISTINCT(last_name)) AS 'numero de nomes repedidos' 
FROM sakila.actor;

-- Ordene os valores na tabela em ordem crescente de sobrenomes 
-- e em ordem decrescente de nome.
(SELECT * FROM sakila.actor) ORDER BY last_name, first_name DESC;






