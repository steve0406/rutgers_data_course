--departments table
create table departments (
	dept_no VARCHAR(5) PRIMARY KEY NOT NULL,
	dept_name VARCHAR(40) NOT NULL

);

--titles table
create table title(
	title_id VARCHAR(5) PRIMARY KEY NOT NULL,
	title VARCHAR(40) NOT NULL
);
--employees table
create  table employees (
	emp_no INT PRIMARY KEY NOT NULL,
	emp_title VARCHAR(5) NOT NULL,
	birth_date DATE  NOT NULL,
	first_name VARCHAR(35) NOT NULL,
	last_name VARCHAR(35) NOT NULL,
	sex VARCHAR(1) NOT NULL,
	hire_date DATE NOT NULL,
	foreign key (emp_title) references title (title_id)
);
--department employee table
create table dept_emp(
	emp_no INT NOT NULL,
	dept_no VARCHAR(5) NOT NULL,
	foreign key (emp_no) references employees (emp_no),
	foreign key (dept_no) references departments (dept_no)
);

--department manager table
create table dept_manager(
	emp_no INT NOT NULL,
	dept_no VARCHAR(5) NOT NULL,
	foreign key (emp_no) references employees (emp_no),
	foreign key (dept_no) references departments (dept_no)
);

--salaries table
create table salaries(
	emp_no INT NOT NULL,
	salary INT NOT NULL,
	foreign key (emp_no) references employees (emp_no)
);

