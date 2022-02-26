create table grupos(
codgrupo varchar(3) primary key,
nombre_grupo varchar(50),
descripcion_grupo text,
estado bool);

insert into grupos(codgrupo,nombre_grupo, descripcion_grupo, estado)
values('G5','SINGRUPO','Este es un grupo de prueba', True);



select * from grupos;