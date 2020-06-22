# Write your MySQL query statement below

SELECT emp.Name AS "Employee"
FROM Employee manager, Employee emp
WHERE emp.ManagerID = manager.Id AND emp.Salary > manager.Salary