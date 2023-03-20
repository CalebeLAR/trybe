-- Exclua do banco de dados o ator com o nome de “KARL”.
SET sql_safe_update=0;
DELETE sakila.actor WHERE first_name = 'KARL';

-- Exclua do banco de dados os atores com o nome de “MATTHEW”.

-- Exclua da tabela film_text todos os registros que possuem a palavra “saga” em suas descrições.

-- Apague da maneira mais performática possível todos os registros das tabelas film_actor e film_category.

-- Inspecione todas as tabelas do banco de dados sakila e analise quais restrições ON DELETE 
-- foram impostas em cada uma. Use o Table Inspector para fazer isso (aba DDL).

-- Exclua o banco de dados e o recrie (use as instruções no início desta aula).