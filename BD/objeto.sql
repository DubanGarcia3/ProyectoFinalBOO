create or replace TYPE nominaobj as object (

	type tab_con is table of empleados%rowtype;
	member procedure add_contratos(id number);
);

create or replace TYPE BODY nominaobj as

	member procedure add_contratos(id number) as
		
	BEGIN
		cursor cur is 
		select * from contratos c
		where c.id_empleado = id_empleado;

		for i in cur
		loop

		end loop

	END;