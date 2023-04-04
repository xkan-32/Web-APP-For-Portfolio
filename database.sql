CREATE DATABASE water_bill_tracker;

USE water_bill_tracker;

CREATE TABLE water_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year_month DATE NOT NULL,
    water_bill FLOAT,
    water_usage FLOAT
);
