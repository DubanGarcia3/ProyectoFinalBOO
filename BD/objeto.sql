CREATE OR REPLACE TYPE contratosobj as OBJECT(
	id number, 
	id_empleado number,
	fecha_inicio Date,
	fecha_fin Date,
	salario number,
	por_com number,
	MEMBER FUNCTION to_string RETURN VARCHAR
);
/
create or replace TYPE BODY contratosobj as
  member function to_string return VARCHAR is
    BEGIN 
    RETURN id || ' ' || id_empleado || ' ' || fecha_inicio  || ' ' || fecha_fin  || ' ' || salario || ' ' || por_com;
  END;
END;
/
