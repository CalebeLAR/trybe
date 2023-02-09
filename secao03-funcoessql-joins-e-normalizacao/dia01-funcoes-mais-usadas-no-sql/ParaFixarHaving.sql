-- Usando a query a seguir, modifique-a de forma que exiba apenas as durações médias que estão 
-- entre 115.0 a 121.50. Além disso, dê um alias (apelido) à coluna gerada por AVG(length), 
-- de forma que deixe a query mais legível. Finalize ordenando os resultados de forma decrescente.
SELECT 
	rating, 
    AVG(length) AS `durações_médias_entre_115.0_a_121.50`
FROM 
	sakila.film
GROUP BY rating 
HAVING `durações_médias_entre_115.0_a_121.50` BETWEEN 115.0 AND 121.50;
-- Usando a query a seguir, exiba apenas os valores de total do custo de substituição que estão 
-- acima de $3950.50. Dê um alias que faça sentido para SUM(replacement_cost), de forma que deixe 
-- a query mais legível. Finalize ordenando os resultados de forma crescente.
SELECT 
    SUM(replacement_cost) AS `custo_de_substituição_acima_de_$3950.50`
FROM
    sakila.film
GROUP BY rating
HAVING `custo_de_substituição_acima_de_$3950.50` > 3950.50
ORDER BY `custo_de_substituição_acima_de_$3950.50` DESC;














-- FIM
