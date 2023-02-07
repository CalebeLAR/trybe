-- Atualize todas as linhas da tabela sakila.actor que possuem o primeiro nome “JULIA” para “JULES”.
SET sql_safe_updates=1, sql_select_limit=500, max_join_size=100000;
UPDATE sakila.actor
	SET first_name = 'JULES OPA'	
WHERE 
	first_name = 'JULES'AND actor_id IN (27, 47);

-- Altere a linha da tabela categoria onde o valor da coluna x é igual “Sci-fi” para “Science Fiction”.
SET sql_safe_updates=0;	
UPDATE sakila.category
	SET `name` = 'AVENTURA'
WHERE 
	`name` = 'Science Fiction';

-- Corrija para $25 o valor do aluguel da tabela filmes com duração maior que 100 minutos e que possuem 
-- classificação “G”, “PG” ou “PG-13” e um custo de substituição maior que $20.
SET sql_safe_updates=0;	
UPDATE sakila.film
	SET replacement_cost = 25.00
WHERE
	length > 100 AND rating IN('G','PG','PG-13') AND replacement_cost > 20.00;

-- Agora, o aluguel dos filmes com duração entre 0 e 100 minutos passará a ser $10,00 e o aluguel dos 
-- filmes com duração acima de 100 minutos passará a ser de $20,00.
SET sql_safe_updates=0;	
UPDATE sakila.film
SET rental_rate = (
    CASE
        WHEN length BETWEEN 1 AND 100 THEN 10
        WHEN length > 100 THEN 20
    END
);


















