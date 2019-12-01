CREATE TABLE empleados(
	id number(10) not null,
	id_lugar number(5) not null,
	nombre varchar2(20) not null,
	apellido varchar2(20) not null,
	genero varchar2(1) not null,
	fecha_nacimiento date not null
);