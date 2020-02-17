CREATE OR REPLACE TYPE EMPLEADO AS OBJECT (
       nombre VARCHAR2(40),
       salario REAL,
       num_hijos INTEGER,
      member FUNCTION get_emp RETURN VARCHAR2,
      member PROCEDURE set_emp(nombreIN IN OUT VARCHAR2,salarioIN IN OUT NUMBER,num_hijosIN IN OUT NUMBER) ,
      member FUNCTION bonificacion RETURN NUMBER
);

CREATE OR REPLACE TYPE BODY EMPLEADO AS

      MEMBER FUNCTION get_emp RETURN VARCHAR2 IS
      BEGIN
        RETURN 'nombre '|| nombre||' salario '|| salario||' numero de hijos'||num_hijos;
      END get_emp;

      MEMBER PROCEDURE set_emp(nombreIN IN OUT VARCHAR2,salarioIN IN OUT NUMBER,num_hijosIN IN OUT NUMBER) IS
      BEGIN
        nombre := nombreIN;
        salario := salarioIN;
        num_hijos := num_hijosIN;
      END set_emp ;

      MEMBER FUNCTION bonificacion RETURN NUMBER IS
      BEGIN
         RETURN (salario/2)*num_hijos;
      END bonificacion ;
END;