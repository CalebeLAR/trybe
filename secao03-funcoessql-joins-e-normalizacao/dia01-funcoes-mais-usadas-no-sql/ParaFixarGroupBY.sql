-- Monte uma query que exiba a quantidade de clientes cadastrados na tabela sakila.customer 
-- que estão ativos e a quantidade que estão inativos.
SELECT active, COUNT(*) AS quantity FROM sakila.customer GROUP BY active;

-- Monte uma query para a tabela sakila.customer que exiba a quantidade de clientes ativos e 
-- inativos por loja. Os resultados devem conter o ID da loja, o status dos clientes (ativos ou inativos)
--  e a quantidade de clientes por status.
SELECT store_id, active, COUNT(*) AS quantity  FROM sakila.customer GROUP BY store_id, active;
--  
-- Monte uma query que exiba a média de duração de locação por classificação indicativa (rating) dos filmes 
-- cadastrados na tabela sakila.film. Os resultados devem ser agrupados pela classificação indicativa e 
-- ordenados da maior média para a menor.
SELECT 
    rating, AVG(rental_duration) AS média_de_duração_de_locação
FROM
    sakila.film
GROUP BY rating
ORDER BY média_de_duração_de_locação DESC;

-- Monte uma query para a tabela sakila.address que exiba o nome do distrito e a quantidade de endereços 
-- registrados nele. Os resultados devem ser ordenados da maior quantidade para a menor.
SELECT 
    district, COUNT(*) AS quantity
FROM
    sakila.address
GROUP BY district
ORDER BY quantity DESC;





















-- fim