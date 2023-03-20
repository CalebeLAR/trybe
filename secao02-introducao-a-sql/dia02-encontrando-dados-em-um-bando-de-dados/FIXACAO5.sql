-- Usando a tabela film:
-- Selecione todos os dados da tabela. Pronto, fez isso? 
-- 1.1 Agora vamos tentar fazer o seguinte: 
-- Crie uma query para encontrar os 20 primeiros filmes, 
-- incluindo o título, o ano de lançamento, a duração, 
-- a classificação indicativa e o custo de substituição. 
-- Ordene os resultados pelos filmes com a maior duração e depois pelo menor 
-- custo de substituição.

SELECT 
	title, release_year, length,rating, replacement_cost 
FROM 
	sakila.film 
ORDER BY length LIMIT 20;

SELECT 
	title, release_year, length,rating, replacement_cost 
FROM 
	sakila.film 
ORDER BY replacement_cost DESC LIMIT 20