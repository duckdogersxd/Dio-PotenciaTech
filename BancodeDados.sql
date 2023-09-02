-- Criação do banco de dados para o cenário de Oficina 

create database oficina;
use oficina;

-- criar tabela cliente
create table clients(
		idClient int auto_increment primary key,
        name varchar(35),
        CPF char(11) not null,
        Address varchar(255),
        constraint unique_cpf_client unique (CPF)
);

alter table clients auto_increment=1;

-- Criar tabela Veiculo

create table vehicle(
		idVehicle int auto_increment primary key,
        idVehicleClient int,
        brand varchar(50),
        model varchar(50),
        yearManufacture year,
        license varchar(10),

        constraint fk_vehicle_client foreign key (idVehicleClient) references clients(idClient)

);

alter table vehicle auto_increment=1;


-- Criar tabela de Ordem de Serviço

create table orders(
	idOrder int auto_increment primary key,
    idOrderVehicle int,
    numOrder int not null,
    dateIssue date,
    amount decimal(10,2),
    orderStatus enum('Cancelado','Confirmado','Em processamento','Finalizado') default 'Em processamento',
    orderDescription varchar(255),
    expectedCompletionDate date,

    constraint fk_ordes_vehicle foreign key (idOrderVehicle) references vehicle(idVehicle)
			on update cascade
);
alter table orders auto_increment=1;


-- Inserir clientes
INSERT INTO clients (name, CPF, Address) VALUES
('João da Silva', '12345678901', 'Rua A, 123'),
('Maria Souza', '98765432101', 'Avenida B, 456'),
('Pedro Oliveira', '45678901201', 'Rua C, 789');

-- Inserir veículos associados aos clientes
INSERT INTO vehicle (idVehicleClient, brand, model, yearManufacture, license) VALUES
(1, 'Ford', 'Fiesta', '2020', 'ABC123'),
(2, 'Chevrolet', 'Cruze', '2019', 'XYZ456'),
(3, 'Volkswagen', 'Golf', '2021', 'LMN789');


-- Inserir ordens de serviço associadas aos veículos
INSERT INTO orders (idOrderVehicle, numOrder, dateIssue, amount, orderDescription, expectedCompletionDate) VALUES
(1, 1001, '2023-08-10', 500.00, 'Troca de óleo e filtro', '2023-08-15'),
(2, 1002, '2023-08-12', 1200.00, 'Reparo do motor', '2023-08-20'),
(3, 1003, '2023-08-15', 800.00, 'Revisão geral', '2023-08-18');


-- SELECT simples
SELECT * FROM clients;
SELECT * FROM orders;
SELECT * FROM vehicle;

-- Utilizando WHERE

-- Recupera as ordens de serviço com status 'Em processamento'
SELECT * FROM orders WHERE orderStatus = 'Em processamento';


-- Utilizando ORDER BY
-- Recupera os clientes ordenados por nome
SELECT * FROM clients ORDER BY name;
-- Recupera as ordens de serviço ordenadas por data de emissão
SELECT * FROM orders ORDER BY dateIssue DESC;
-- Recupera os veículos ordenados por ano de fabricação e marca
SELECT * FROM vehicle ORDER BY yearManufacture, brand;

-- Utilizando HAVING e gerando atributo derivado
-- Recupera a média de valor das ordens de serviço por cliente com média superior a 800
SELECT idOrderVehicle, AVG(amount) AS mediaValor
FROM orders
GROUP BY idOrderVehicle
HAVING AVG(amount) > 800;

-- Utilizando Join
-- Recupera a lista de veículos com informações do proprietário
SELECT V.*, C.name AS NomeProprietario
FROM vehicle V
INNER JOIN clients C ON V.idVehicleClient = C.idClient;
