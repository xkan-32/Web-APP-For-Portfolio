
USE water_bill_tracker;

CREATE TABLE water_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    `year_month` DATE NOT NULL,
    water_bill DECIMAL(10, 2) NOT NULL,
    water_usage INT NOT NULL
);

