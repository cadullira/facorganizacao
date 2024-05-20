CREATE TABLE tbl1(
	one text,
	two int
);

INSERT INTO tbl1 VALUES(
	'hello', 10
);

INSERT INTO tbl1 VALUES(
	'good bye', 20
);

SELECT * FROM tbl1;

CREATE TABLE IF NOT EXISTS employees (

        first_name VARCHAR(15) NOT NULL,

        mid_name CHAR,

        last_name VARCHAR(15) NOT NULL,

        cpf CHAR(11) NOT NULL,

        birthday DATE,

        street_address VARCHAR(30),

        gender CHAR,

        salary DECIMAL(10, 2),

        supervisor_cpf CHAR(11),

        department_number INT NOT NULL,

        PRIMARY KEY (cpf)

    );
    
 CREATE TABLE IF NOT EXISTS projects(

        project_name VARCHAR(15) NOT NULL,

        project_number INT NOT NULL,

        project_local VARCHAR(15),

        PRIMARY KEY (project_number)

    );



CREATE TABLE IF NOT EXISTS employee_projects(

        employee_cpf CHAR(11) NOT NULL,

        project_number INT NOT NULL,

        time_spent DECIMAL(3, 1) NOT NULL,

        PRIMARY KEY (employee_cpf, project_number),

        Foreign Key (employee_cpf) REFERENCES employees(cpf),

        Foreign Key (project_number) REFERENCES projects(project_number)

    );
    
 
 
INSERT INTO

    employees (

        first_name,

        mid_name,

        last_name,

        cpf,

        birthday,

        street_address,

        gender,

        salary,

        supervisor_cpf,

        department_number

    )

VALUES (

        'João',

        NULL,

        'Silva',

        '123955724313',

        '1990-01-15',

        'Rua das Flores, 123',

        'M',

        5000.00,

        '98765432101',

        1

    );



