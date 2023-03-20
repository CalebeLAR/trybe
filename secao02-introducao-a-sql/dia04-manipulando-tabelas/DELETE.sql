-- Excluindo dados de uma tabela
DELETE FROM banco_de_dados.tabela
WHERE coluna = 'valor'; -- O WHERE é opcional. Porém, sem ele, todas as linhas da tabela seriam excluídas.

SET SQL_SAFE_UPDATES = 0;
DELETE FROM sakila.film_text
WHERE title = 'ACADEMY DINOSAUR';

DELETE VS TRUNCATE

