
ALTER TABLE contratos ADD(
    CONSTRAINT cont_pk_idc PRIMARY KEY(id),
    CONSTRAINT cont_fk_ide FOREIGN KEY(id_empleado) REFERENCES empleados(id)
);