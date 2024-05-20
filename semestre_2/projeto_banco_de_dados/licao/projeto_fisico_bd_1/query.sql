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
    
    
CREATE TABLE

    IF NOT EXISTS employees (

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



CREATE TABLE

    IF NOT EXISTS projects(

        project_name VARCHAR(15) NOT NULL,

        project_number INT NOT NULL,

        project_local VARCHAR(15),

        PRIMARY KEY (project_number)

    );



CREATE TABLE

    IF NOT EXISTS employee_projects(

        employee_cpf CHAR(11) NOT NULL,

        project_number INT NOT NULL,

        time_spent DECIMAL(3, 1) NOT NULL,

        PRIMARY KEY (employee_cpf, project_number),

        Foreign Key (employee_cpf) REFERENCES employees(cpf) ON UPDATE CASCADE ON DELETE CASCADE,

        Foreign Key (project_number) REFERENCES projects(project_number)

    );
    
INSERT INTO employees (first_name, mid_name, last_name, cpf, birthday, street_address, gender, salary, supervisor_cpf, department_number)

VALUES ('João', 'A', 'Silva', '12345678901', '1990-05-15', 'Rua das Flores, 123', 'M', 5000.00, NULL, 1);



INSERT INTO employees (first_name, mid_name, last_name, cpf, birthday, street_address, gender, salary, supervisor_cpf, department_number)

VALUES ('Maria', 'B', 'Santos', '98765432109', '1985-12-03', 'Avenida Central, 456', 'F', 6000.00, '12345678901', 1);

--------------------------------------------------------------------------------------



INSERT INTO projects (project_name, project_number, project_local)

VALUES ('Projeto A', 1, 'Fortaleza');



INSERT INTO projects (project_name, project_number, project_local)

VALUES ('Projeto B', 2, 'Recife');

--------------------------------------------------------------------------------------

INSERT INTO employee_projects (employee_cpf, project_number, time_spent)

VALUES ('12345678901', 1, 80.5);



INSERT INTO employee_projects (employee_cpf, project_number, time_spent)

VALUES ('12345678901', 2, 65.0);



INSERT INTO employee_projects (employee_cpf, project_number, time_spent)

VALUES ('98765432109', 2, 50.2);

PRAGMA foreign_keys = ON;



