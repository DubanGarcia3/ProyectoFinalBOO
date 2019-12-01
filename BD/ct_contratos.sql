CREATE TABLE contratos(
	id number(4) not null,
	id_empleado number(10) not null,
	fecha_inicio date not null,
	fecha_fin date,
	salario number(10, 2),
	porc_com number(2)
);