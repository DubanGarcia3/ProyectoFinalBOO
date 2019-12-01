CREATE USER pf identified by pf;
GRANT CONNECT, RESOURCE TO pf;
CONN pf/pf;

@ct_empleados;
@ct_contratos;

@cc_empleados;
@cc_contratos;

@insdb;