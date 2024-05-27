/* ESTUDANTES */
CREATE TABLE students(
  student_id INT NOT NULL,
  first_name VARCHAR(50) NOT NULL ,
  last_name VARCHAR(50) NOT NULL ,
  email VARCHAR(50) NOT NULL,
  date_of_birth DATE,
  gender CHAR(1),
  PRIMARY KEY (student_id)
);

/* INSTRUTORES */
CREATE TABLE instructors(
  instructor_id INT NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR (50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  date_of_birth DATE,
  hire_date DATE,
  department VARCHAR(50),
  PRIMARY KEY (instructor_id)
);

/* CURSOS */
CREATE TABLE courses(
  course_id INT NOT NULL,
  course_name VARCHAR(50) NOT NULL,
  department VARCHAR(50),
  credits INT,
  instructor_id INT NOT NULL,
  PRIMARY KEY (course_id),
  FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON UPDATE CASCADE ON DELETE CASCADE,
);

/* MATRÍCULAS */
CREATE TABLE enrollments(
  enrollment_id INT NOT NULL,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  enrollment_date DATE,
  grade DECIMAL(4, 2),
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON UPDATE CASCADE ON DELETE CASCADE,
);

/* LIVROS */
CREATE TABLE books(
  book_id INT,
  title VARCHAR(100) NOT NULL,
  author VARCHAR(50),
  publication_date DATE,
  genre VARCHAR(50),
  price DECIMAL(6, 2) NOT NULL,
  PRIMARY KEY(book_id),
);

/* AVALIAÇÕES */
CREATE TABLE book_reviews(
  review_id INT,
  book_id INT NOT NULL,
  student_id INT NOT NULL,
  review_date DATE,
  rating INT,
  review_text VARCHAR(500),
  PRIMARY KEY (review_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON UPDATE CASCADE ON DELETE CASCADE,
);

/* FUNCIONÁRIOS */
CREATE TABLE employees(
  employee_id INT,
  firs_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  date_of_birth DATE NOT NULL,
  job_title VARCHAR(50) NOT NULL,
  hire_date DATE,
  salary DECIMAL (8, 2),
  PRIMARY KEY (employee_id)
);

/* DEPARTAMENTOS */
CREATE TABLE bookstore_departments(
  department_id INT,
  department_name VARCHAR(50) NOT NULL,
  manager_id INT NOT NULL,
  lacation VARCHAR(100),
  PRIMARY KEY(department_id),
  FOREIGN KEY (manager_id) REFERENCES employees(employee_id) ON UPDATE CASCADE ON DELETE CASCADE,
);

/* CLIENTES */
CREATE TABLE customers(
  customer_id INT,
  customer_name VARCHAR(100) NOT NULL,
  andress VARCHAR(100),
  age INT,
  PRIMARY KEY (customer_id),
);

/* PEDIDOS */
/* DECIMAL (TOTAL DE DÍGITOS, DÍGITOS APÓS A DIREITA )*/
CREATE TABLE orders(
  order_id INT,
  customer_id INT NOT NULL,
  order_date DATE,
  total_amount DECIMAL(8, 2) NOT NULL,
  shipping_andress VARCHAR(100),
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON UPDATE CASCADE ON DELETE CASCADE
);

/* ORDEM DE PEDIDO */
CREATE TABLE order_items(
  item_id INT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(8, 2) NOT NULL,
  PRIMARY KEY (item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON UPDATE CASCADE ON DELETE CASCADE
  FOREIGN KEY (product_id) REFERENCES books(book_id)
);