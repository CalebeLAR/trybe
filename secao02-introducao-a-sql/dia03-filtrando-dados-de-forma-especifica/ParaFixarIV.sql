-- Quantos pagamentos temos com a data de retorno 2005-05-25? 
-- Há múltiplas maneiras possíveis de encontrar a resposta.
SELECT COUNT(*) Pagamentos FROM sakila.payment
WHERE DATE(payment_date) = '2005-05-25';
    
SELECT 
	COUNT(*) pagamentos
FROM 
	sakila.payment
WHERE 
	payment_date LIKE '2005-05-25%';

-- Quantos pagamentos foram feitos entre 01/07/2005 e 22/08/2005?
SELECT COUNT(*) FROM sakila.payment 
WHERE payment_date BETWEEN '2005-07-01 00:00:00' AND '2005-08-22 23:59:59';

-- Usando a tabela rental, extraia data, ano, mês, dia, hora, minuto e segundo 
-- dos registros com rental_id = 10330. Utilize a coluna rental_date para extrair as 
-- informações.
SELECT 
	CONCAT(
        YEAR(rental_date),"-->","ANO","  ",
        MONTH(rental_date),"-->","MES","  ",
        DAY(rental_date),"-->","DIA","  ",
        HOUR(rental_date),"-->","HORA","  ",
        MINUTE(rental_date),"-->","MINUTO","  ",
        SECOND(rental_date),"-->","SEGUNDO"
	) AS 'datas completas'
FROM sakila.rental WHERE rental_id = 10330;

SELECT DATE(rental_date) AS Data,
YEAR(rental_date) AS Ano ,
MONTH(rental_date) AS Mes,
DAY(rental_date) AS Dia,
HOUR(rental_date) AS Hora,
MINUTE(rental_date) AS Minuto,
SECOND(rental_date) AS Segundo
FROM sakila.rental
WHERE rental_id = 10330;

-- Monte uma query que retorne todos os dados do pagamento feito no dia 28/07/2005 
-- a partir das 22 horas.

SELECT * FROM sakila.rental WHERE rental_date LIKE '2005-07-28 22%';

USE sakila;
SELECT * FROM sakila.payment
WHERE DATE(payment_date) = '2005-07-28' AND HOUR(payment_date) >= 22;











