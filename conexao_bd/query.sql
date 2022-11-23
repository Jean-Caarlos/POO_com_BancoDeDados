CREATE TABLE username_cartao
(
    id int IDENTITY NOT NULL,
    id_proprietario int NOT NULL,
    creditos FLOAT NOT NULL,
    tipo VARCHAR(30) NOT NULL,
    data_emissao DATE NOT NULL
);

CREATE TABLE username_usuario
(
    id int IDENTITY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL
);

CREATE TABLE username_motorista
(
    id int IDENTITY NOT NULL,
    cnh int NOT NULL,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL
);


CREATE TABLE username_onibus
(
    id int IDENTITY NOT NULL,
    id_motorista int NOT NULL,
    placa int NOT NULL,
    numero_linha int NOT NULL,
    modelo VARCHAR(30) NOT NULL,
    ano_fabricacao DATE NOT NULL
);
