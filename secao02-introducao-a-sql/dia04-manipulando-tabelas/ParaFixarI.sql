-- Insira um novo funcionário na tabela sakila.staff.
-- Para saber quais campos são obrigatórios, clique com o botão direito na tabela sakila.staff 
-- e selecione Table Inspector. Clique na aba columns e verifique quais campos aceitam nulos para te guiar. 
-- Lembre-se de que valores que são gerados automaticamente não precisam ser inseridos manualmente.
INSERT INTO `sakila`.`staff` 
	(staff_id, first_name, last_name, address_id, email, store_id, active, username,`password`, last_update)
VALUES
	(null, 'calebe', 'ribeiro', 23,'ca6ele@gmail.com',1, 1, 'ca6ele', 'senha', null);

-- Feito o exercício anterior, vamos agora para o nível 2. Insira dois funcionários novos em apenas uma query.
-- Selecione os cinco primeiros nomes e sobrenomes da tabela sakila.customer e cadastre essas pessoas como 
-- atores na tabela sakila.actor.
INSERT INTO `sakila`.`staff` 
	(first_name, last_name, address_id, email, store_id, active, username, `password`)
VALUES 
	('luis','humberto',1,'luis@gmail.com',2,1,'lus21','senhaLuis'),
	('Mariana','Botelho',2,'MariB@mail.com',1,2,'Mari','senhaMari');

-- Cadastre três categorias de uma vez só na tabela sakila.category.
INSERT INTO `sakila`.`category` 
	(`name`)
VALUE
	('Antonio Botelho');
    
INSERT INTO `sakila`.`category` 
	(`name`)
SELECT
	CONCAT(first_name," ", last_name)
FROM sakila.staff
LIMIT 2;

-- Cadastre uma nova loja na tabela sakila.store.
INSERT INTO `sakila`.`store` 
	(manager_staff_id, address_id)
VALUE
	(3, 2);





















