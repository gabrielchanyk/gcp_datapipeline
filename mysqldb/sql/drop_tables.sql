-- Drop CellularUsage table first, as it references Customers
DROP TABLE IF EXISTS CellularUsage;

-- Drop InternetUsage table next, as it references Customers
DROP TABLE IF EXISTS InternetUsage;

-- Drop Billing table, as it references Customers
DROP TABLE IF EXISTS Billing;

-- Finally, drop the Customers table
DROP TABLE IF EXISTS Customers