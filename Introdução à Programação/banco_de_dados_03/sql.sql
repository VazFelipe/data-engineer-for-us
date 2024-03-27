CREATE TABLE carros (
  id_carro SERIAL PRIMARY KEY,
  nome VARCHAR(24) NOT NULL,
  preco FLOAT NOT NULL,
  promocional BOOLEAN
);
COMMIT;

CREATE TABLE vendedor (
  id_vendedor SERIAL PRIMARY KEY,
  nome VARCHAR(24) NOT NULL,
  cpf VARCHAR(11) NOT NULL
);
COMMIT;

INSERT INTO carros 
	(nome, preco, promocional)
VALUES
	('BMW', 180000, FALSE),
	('Ferrari', 900000, TRUE);
COMMIT;

INSERT INTO vendedor 
	(nome, cpf)
VALUES
	('Felipe', '01234567890'),
	('José', '12345678910');
COMMIT;

SELECT * FROM carros;
COMMIT;
SELECT * FROM vendedor;
COMMIT;

--DROP TABLE carros;
--DROP TABLE vendedor;