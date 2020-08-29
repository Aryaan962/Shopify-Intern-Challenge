-- Solution 1
SELECT COUNT(ShipperID)
FROM Orders
WHERE ShipperID = (
    SELECT shipperID
    FROM Shippers
    WHERE ShipperName = 'Speedy Express'
);

/*
* Return value for how many orders were shipped by speedy express is 54.
*/


-- Solution 2
SELECT Employees.LastName, COUNT(Orders.EmployeeID) AS NumberSold
FROM Orders
JOIN Employees
ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY LastName
ORDER BY NumberSold DESC
LIMIT 1;

/*
* Return value for the last name of the employee with the most orders is Peacock.
*/

-- Solution 3
SELECT OrderDetails.ProductID, Orders.OrderID, COUNT(Orders.CustomerID) AS NumberOfOrders, Orders.CustomerID, Products.ProductName
FROM Orders
JOIN OrderDetails
ON Orders.OrderID = OrderDetails.OrderID
JOIN Products
ON OrderDetails.ProductID = Products.ProductID
WHERE CustomerID IN (
	SELECT CustomerID
	FROM Customers
	WHERE Country = 'Germany'
)
GROUP BY CustomerID
ORDER BY NumberOfOrders DESC
LIMIT 1;

/*
* Return value for the product most ordered by people in Germany was Ikura.
*/
