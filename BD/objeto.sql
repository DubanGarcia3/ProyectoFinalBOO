create or replace TYPE contratosobj as object (
	id number, 
	id_empleado number,
	fecha_inicio Date,
	fecha_fin Date,
	salario number,
	por_com number,
	member function to_string() return varchar;

);

create or replace TYPE BODY contratosobj as
	member function to_string() return varchar
		BEGIN 
		RETURN id || ' ' || id_empleado || ' ' || fecha_inicio  || ' ' || fecha_fin  || ' ' || salario || ' ' || por_com;
	END;
END;