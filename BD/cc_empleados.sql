ALTER TABLE empleados ADD(
	CONSTRAINT emp_pk_id PRIMARY KEY(id),
	CONSTRAINT emp_ck_gen CHECK(genero IN('F'/*Femenimo*/, 'M'/*Masculino*/))
);