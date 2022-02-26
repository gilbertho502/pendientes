
create table usuarios(
	cod_usuario varchar (4) primary key,
	username varchar (20),
	email varchar (20),
	password varchar(8)
);

select * from usuarios;

insert into usuarios(cod_usuario, username, email, password)
values('A100','admin','admin@gmail.com', '123');

insert into usuarios(cod_usuario, username, email, password)
values('A200','operador','operador@gmail.com', '456');

insert into usuarios(cod_usuario, username, email, password)
values('A300','sisteas','sistemas@gmail.com', '123');