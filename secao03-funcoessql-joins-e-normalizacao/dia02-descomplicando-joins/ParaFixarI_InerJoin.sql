-- Monte uma query que exiba o id do ator, nome do ator e id do filme em que ele já atuou, 
-- usando as tabelas actor e film_actor.
SELECT 
    a.actor_id, a.first_name, f.film_id
FROM
    sakila.actor AS a
INNER JOIN
	sakila.film_actor AS f
ON a.actor_id = f.actor_id;
-- Use o JOIN para exibir o nome, sobrenome e endereço de cada um dos funcionários do banco. 
-- Use as tabelas staff e address.
SELECT 
    CONCAT(s.first_name, ' ', s.last_name) AS 'nome completo',
    a.address,
    a.district
FROM
    sakila.staff AS s
INNER JOIN 
	sakila.address AS a
ON 
	s.address_id = a.address_id;

-- Exiba o id do cliente, nome e email dos primeiros 100 clientes, ordenados pelo nome em ordem decrescente, 
-- juntamente com o id do endereço e o nome da rua onde o cliente mora. Essas informações podem ser 
-- encontradas nas tabelas customer e address.
SELECT 
    c.first_name, c.email, a.address_id, a.district
FROM
    sakila.customer AS c
        INNER JOIN
    sakila.address AS a ON a.address_id = c.address_id
ORDER BY first_name DESC
LIMIT 100;

-- Exiba o nome, email, id do endereço, endereço e distrito dos clientes que moram no distrito da 
-- California e que contêm “rene” em seus nomes. As informações podem ser encontradas nas tabelas 
-- address e customer.
SELECT 
    c.first_name, c.email,
    a.address_id, a.address, a.district
FROM
    sakila.customer AS c
        INNER JOIN
    sakila.address AS a ON c.address_id = a.address_id
WHERE a.district = 'California' AND c.first_name LIKE '%rene%';

-- Exiba o nome, o sobrenome e a quantidade de filmes alugados por cada cliente cadastrado. 
-- Ordene seus resultados por nome e sobrenome de forma decrescente. Exiba somente os clientes ativos. 
-- As informações podem ser encontradas nas tabelas customer e rental.
SELECT 
	c.first_name, c.last_name, COUNT(*) AS `filmes_cadastrados`
FROM 
	sakila.rental AS r
		INNER JOIN
	sakila.customer AS c ON r.customer_id = c.customer_id
WHERE 
	c.active = 1
GROUP BY 
	c.first_name, c.last_name;
    
-- Monte uma query que exiba o nome, sobrenome e a média de valor (amount) paga aos 
-- funcionários no ano de 2006. Use as tabelas payment e staff. Os resultados devem estar 
-- agrupados pelo nome e sobrenome do funcionário.
SELECT 
    s.first_name, s.last_name, AVG(p.amount)
FROM
	sakila.payment AS p
        INNER JOIN
    sakila.staff AS s ON p.staff_id = s.staff_id
WHERE 
	YEAR(p.payment_date) = '2006'
GROUP BY 
	s.first_name, s.last_name;

-- Monte uma query que exiba o id do ator, nome, id do filme e título do filme, usando as 
-- tabelas actor, film_actor e film. Dica: você precisará fazer mais de um JOIN na mesma query.
SELECT 
    ac.actor_id, ac.first_name, ac.last_name,
	fa.film_id
FROM
   sakila.film_actor AS fa
        INNER JOIN
    sakila.actor AS ac ON fa.actor_id = ac.actor_id
		INNER JOIN 
	sakila.film AS fi ON fa.film_id = fi.film_id;




























-- fim