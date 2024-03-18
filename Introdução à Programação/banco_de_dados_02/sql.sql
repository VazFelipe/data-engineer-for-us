CREATE TABLE instrumentos (
  id_instrumento SERIAL PRIMARY KEY,
  nome VARCHAR(24) NOT NULL,
  preco FLOAT NOT NULL,
  em_promocao BOOLEAN
);
COMMIT;

CREATE TABLE vendedor (
  id_vendedor SERIAL PRIMARY KEY,
  nome VARCHAR(24) NOT NULL,
  cpf VARCHAR(11) NOT NULL
);
COMMIT;

INSERT INTO instrumentos 
	(nome, preco, em_promocao)
VALUES
	('Gibson', 18000, FALSE),
	('Fender', 20000, TRUE);
COMMIT;

INSERT INTO vendedor 
	(nome, cpf)
VALUES
	('Marshall', '01234567890'),
	('Lorran', '12345678910');
COMMIT;

SELECT * FROM instrumentos;
COMMIT;
SELECT * FROM vendedor;
COMMIT;

--DROP TABLE instrumentos;
--DROP TABLE vendedor;
