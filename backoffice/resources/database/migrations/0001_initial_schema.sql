CREATE TABLE Product (
	prod_id          VARCHAR( 40 ) NOT NULL,
	prod_name        VARCHAR( 40 ) NOT NULL,
	prod_price       INT UNSIGNED NOT NULL,
	prod_description VARCHAR( 40 ) NOT NULL,
	prod_status      TINYINT UNSIGNED NOT NULL,
	rest_id          VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( prod_id )
);

CREATE TABLE Restaurant (
	rest_id     VARCHAR( 40 ) NOT NULL,
	rest_name   VARCHAR( 40 ) DEFAULT NULL,
	rest_status TINYINT UNSIGNED NOT NULL,
	PRIMARY KEY( rest_id )
);

CREATE TABLE Employee (
    emp_id     VARCHAR( 40 ) NOT NULL,
	emp_email  VARCHAR( 60 ) NOT NULL,
	emp_name   VARCHAR( 40 ) NOT NULL,
	emp_role   TINYINT UNSIGNED NOT NULL,
	emp_status TINYINT UNSIGNED NOT NULL,
	rest_id    VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( emp_id )
);

CREATE TABLE Dining_Table (
	tab_id          VARCHAR( 40 ) NOT NULL,
	tab_number      TINYINT UNSIGNED NOT NULL,
	tab_description VARCHAR( 40 ) NOT NULL,
	tab_status      TINYINT UNSIGNED NOT NULL,
	rest_id         VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( tab_id )
);

ALTER TABLE Product      ADD CONSTRAINT FK_Product_Restaurant FOREIGN KEY ( rest_id ) REFERENCES Restaurant( rest_id );
ALTER TABLE Employee     ADD CONSTRAINT FK_Employee_Restaurant FOREIGN KEY ( rest_id ) REFERENCES Restaurant( rest_id );
ALTER TABLE Dining_Table ADD CONSTRAINT FK_Dining_Table_Restaurant FOREIGN KEY ( rest_id ) REFERENCES Restaurant( rest_id );