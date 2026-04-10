-- select (select distinct salary from employee order by salary desc limit 1 offset 1) as secondhighestsalary;

select max(salary) as secondhighestsalary from employee where salary < (SELECT MAX(salary) FROM employee) order by salary desc limit 1;
