CREATE TABLE User (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    UserType ENUM('Admin', 'Employee') NOT NULL,
    Email VARCHAR(100) NOT NULL,
    DateJoined DATE
);

CREATE TABLE Patient (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    DateOfBirth DATE,
    Gender ENUM('Male', 'Female', 'Other'),
    Address VARCHAR(255),
    ContactNumber VARCHAR(20),
    Email VARCHAR(100),
    PrescriptionID INT,
    FOREIGN KEY (PrescriptionID) REFERENCES Prescription(PrescriptionID)
);

for Doctor:- 

CREATE TABLE Doctor (
    DoctorID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Specialization VARCHAR(100),
    ContactNumber VARCHAR(20),
    Email VARCHAR(100)
);

for prescription :- 

CREATE TABLE Prescription (
    PrescriptionID INT PRIMARY KEY AUTO_INCREMENT,
    PatientID INT,
    DoctorID INT,
    DatePrescribed DATE,
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID)
);

for medicine:- 

CREATE TABLE Medicine (
    MedicineID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Description VARCHAR(255),
    Manufacturer VARCHAR(100),
    UnitPrice DECIMAL(10,2),
    Quantity INT,
    ExpiryDate DATE
);


for inventory :- 

CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY AUTO_INCREMENT,
    MedicineID INT,
    Quantity INT,
    ExpiryDate DATE,
    FOREIGN KEY (MedicineID) REFERENCES Medicine(MedicineID)
);

for sale:- 

CREATE TABLE Sale (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,
    PatientID INT,
    MedicineID INT,
    Quantity INT,
    SaleDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    FOREIGN KEY (MedicineID) REFERENCES Medicine(MedicineID)
);

for supplier : -

CREATE TABLE Supplier (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    ContactNumber VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255)
);

for purchase :- 

CREATE TABLE Purchase (
    PurchaseID INT PRIMARY KEY AUTO_INCREMENT,
    SupplierID INT,
    MedicineID INT,
    Quantity INT,
    PurchaseDate DATE,
    TotalCost DECIMAL(10,2),
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID),
    FOREIGN KEY (MedicineID) REFERENCES Medicine(MedicineID)
);

for emplyoee :- 

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Position VARCHAR(100),
    DateOfBirth DATE,
    Gender ENUM('Male', 'Female', 'Other'),
    Address VARCHAR(255),
    ContactNumber VARCHAR(20),
    Email VARCHAR(100),
    DateJoined DATE
);

for employee scedule :- 

CREATE TABLE EmployeeSchedule (
    ScheduleID INT PRIMARY KEY AUTO_INCREMENT,
    EmployeeID INT,
    Date DATE,
    StartTime TIME,
    EndTime TIME,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

for transaction log :- 

CREATE TABLE TransactionLog (
    LogID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
    Action VARCHAR(255),
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);
