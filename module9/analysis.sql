--List the employee number, last name, first name, sex, 
--and salary of each employee.
select e.emp_no, e.last_name, e.first_name, e.sex, s.salary
from employees as e 
inner join salaries as s
on e.emp_no = s.emp_no
order by e.emp_no;

--List the first name, last name, and 
--hire date for the employees who were hired in 1986.
select emp_no, last_name, first_name, hire_date
from employees
where extract(year from hire_date) = 1986;

--List the manager of each department along with their 
--department number, department name, employee number, 
--last name, and first name.

SELECT d.dept_no, d.dept_name, e.emp_title, e.last_name, e.first_name
FROM dept_emp as de
LEFT JOIN employees as e
ON e.emp_no = de.emp_no
LEFT JOIN departments as d
ON d.dept_no = de.dept_no
WHERE e.emp_title LIKE 'm%'
;

--List the department number for each employee along
--with that employee’s employee number, last name, 
--first name, and department name.

select distinct on (e.emp_no) e.emp_no, e.last_name, e.first_name,d.dept_name
from employees as e
left join dept_emp as de
on e.emp_no = de.emp_no
inner join departments as d
on de.dept_no = d.dept_no
order by e.emp_no DESC;

--List first name, last name, and 
--sex of each employee whose first name
--is Hercules and whose last name begins with the letter B.

select e.last_name, e.first_name
from employees as e 
where (e.first_name = 'Hercules') and (lower(e.last_name) like 'b%')
order by e.last_name;

--List each employee in the Sales department,
--including their employee number, last name, and first name.

select e.emp_no, e.last_name,e.first_name,d.dept_name
from employees as e 
inner join dept_emp as cd
on e.emp_no = cd.emp_no
inner join departments as d
on cd.dept_no = d.dept_no
where lower(d.dept_name) = 'sales';

--List each employee in the Sales and Development departments, 
--including their employee number, last name, first name, 
--and department name.

select e.emp_no, e.last_name,e.first_name,d.dept_name
from employees as e 
inner join dept_emp as cd
on e.emp_no = cd.emp_no
inner join departments as d
on cd.dept_no = d.dept_no
where (lower(d.dept_name) = 'sales') or(lower(d.dept_name)= 'development') ;

--List the frequency counts, in descending order,
--of all the employee last names 
--(that is, how many employees share each last name).

select last_name,count(last_name) as Frequency
from employees
group by last_name
order by frequency desc;