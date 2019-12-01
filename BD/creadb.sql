CREATE USER pf identified by pf;
GRANT CONNECT, RESOURCE TO pf;
CONN pf/pf;

@ct_empleados;
@ct_contratos;
@ct_nominas;

@cc_empleados;
@cc_contratos;

@objeto;

--@ins_empleados;
--@ins_contratos;