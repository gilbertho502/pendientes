create database cargamossalud encoding 'utf-8';

create table pacientes(
id_paciente varchar(3) not null primary key,
nombre varchar(100),
	edad integer check(edad between 18 and 75),
	dni varchar(10) not null unique
);

create table enfermedades(
	id_enfermedad serial primary key,
	nombre varchar(20)
);

create table tratamientos(
	id_tra serial primary key,
	nombre varchar(150),
	estado boolean default True
);

create table pac_enf(
	id_pa_enf serial primary key,
	id_paciente varchar(3),
	id_enfermedad integer,
	costo_total decimal(6,2)

);


alter table pac_enf add constraint fk_paciente 
foreign key (id_paciente) references pacientes(id_paciente);

alter table pac_enf add constraint fk_enfermedad 
foreign key (id_enfermedad) references enfermedades(id_enfermedad);

alter table pac_enf drop constraint fk_pacientes

INSERT INTO pacientes (id_paciente,nombre,edad,DNI) VALUES(101,'PEPE',41,'1111111');
INSERT INTO pacientes (id_paciente,nombre,edad,DNI) VALUES(103,'PILI',32,'3333333');
INSERT INTO pacientes (id_paciente,nombre,edad,DNI) VALUES(105,'PEPE',47,'5555555');
INSERT INTO pacientes (id_paciente,nombre,edad,DNI) VALUES(107,'LUIS',42,'7777777');
INSERT INTO pacientes (id_paciente,nombre,edad,DNI) VALUES(109,'PACO',21,'9999999');

select * from pacientes;

INSERT INTO enfermedades (id_enfermedad,nombre) VALUES(1,'Colitis');
INSERT INTO enfermedades (id_enfermedad,nombre) VALUES(3,'Almosapos');
INSERT INTO enfermedades (id_enfermedad,nombre) VALUES(5,'Rabitis');
INSERT INTO enfermedades (id_enfermedad,nombre) VALUES(7,'Psicoseborrea');
INSERT INTO enfermedades (id_enfermedad,nombre) VALUES(9,'Kanofobia');

select * from enfermedades;

INSERT INTO tratamientos (id_tra, nombre) VALUES(11,'Barros');     
INSERT INTO tratamientos (id_tra, nombre) VALUES(21,'Algas');     
INSERT INTO tratamientos (id_tra, nombre) VALUES(31,'Lunares'); 

select * from tratamientos;

INSERT INTO pac_enf (id_paciente,id_enfermedad,costo_total) VALUES(101,1, 4.0);     
INSERT INTO pac_enf (id_paciente,id_enfermedad,costo_total) VALUES(101,5, 6.0);     
INSERT INTO pac_enf (id_paciente,id_enfermedad,costo_total) VALUES(101,7, 5.0);     
INSERT INTO pac_enf (id_paciente,id_enfermedad,costo_total) VALUES(105,1, 5.0);
INSERT INTO pac_enf (id_paciente,id_enfermedad,costo_total) VALUES(109,1, 3.0);     
INSERT INTO pac_enf (id_paciente,id_enfermedad,costo_total) VALUES(109,3, 7.0);  

select * from pac_enf;


create table pac_enf_trat(
	ip_pac_enf_trat serial primary key,
	id_paciente varchar(3),
	id_enfermedad integer,
	id_tra integer,
	costo decimal(6,2),
	foreign key (id_paciente) references pacientes (id_paciente)
	on delete cascade
	on update cascade,
	foreign key (id_enfermedad) references enfermedades (id_enfermedad)
	on delete cascade
	on update cascade

);


INSERT INTO pac_enf_trat (id_paciente,id_enfermedad,id_tra,costo) VALUES(101,1,11, 3);     
INSERT INTO pac_enf_trat (id_paciente,id_enfermedad,id_tra,costo) VALUES(101,1,21, 5);     
INSERT INTO pac_enf_trat (id_paciente,id_enfermedad,id_tra,costo) VALUES(101,5,31, 6);  
INSERT INTO pac_enf_trat (id_paciente,id_enfermedad,id_tra,costo) VALUES(101,7,21,6);     
INSERT INTO pac_enf_trat (id_paciente,id_enfermedad,id_tra,costo) VALUES(101,7,31,6);     
INSERT INTO pac_enf_trat (id_paciente,id_enfermedad,id_tra,costo) VALUES(105,1,11,5.0);     
INSERT INTO pac_enf_trat (id_paciente,id_enfermedad,id_tra,costo) VALUES(105,1,21,7.0);     
INSERT INTO pac_enf_trat (id_paciente,id_enfermedad,id_tra,costo) VALUES(109,1,11,5.0);
INSERT INTO pac_enf_trat (id_paciente,id_enfermedad,id_tra,costo) VALUES(109,3,21,5.0);

select * from pac_enf_trat

select * from pacientes;
select nombre,dni from pacientes;
select * from pacientes where edad >45;
select * from pacientes where dni = '1111111';
select * from pacientes where edad between 18 and 40;
select * from pacientes order by nombre;
select * from pacientes order by nombre desc;
select * from pacientes order by edad;
select * from pacientes where nombre= 'PEPE' or nombre= 'LUIS';
select * from pacientes where nombre in('PEPE', 'LUIS');
update pacientes set dni='' where id_paciente= '101'
select * from pacientes where dni is null;
update pacientes set dni='1111111' where id_paciente= '101'

select * from pacientes;
select * from enfermedades;
select * from pac_enf;

select p.nombre, e.nombre from pacientes p inner join pac_enf pe on p.id_paciente = pe.id_paciente 
inner join enfermedades e on pe.id_enfermedad = e.id_enfermedad;
























