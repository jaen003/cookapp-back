CREATE TABLE Dining_Table (
	tab_id     VARCHAR( 40 ) NOT NULL,
	tab_number TINYINT NOT NULL,
	tab_status TINYINT NOT NULL,
	rest_id    VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( tab_id )
);

CREATE TABLE Invoice (
	inv_id     VARCHAR( 40 ) NOT NULL,
	inv_status TINYINT NOT NULL,
	tab_id     VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( inv_id )
);

CREATE TABLE Product (
	prod_id     VARCHAR( 40 ) NOT NULL,
	prod_name   VARCHAR( 40 ) NOT NULL,
	prod_status TINYINT NOT NULL,
	PRIMARY KEY( prod_id )
);

CREATE TABLE Food_Order (
	ord_id          VARCHAR( 40 ) NOT NULL,
	ord_amount      TINYINT NOT NULL,
	ord_description VARCHAR( 200 ) NOT NULL,
	ord_status      TINYINT NOT NULL,
	inv_id          VARCHAR( 40 ) NOT NULL,
	prod_id         VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( ord_id )
);

ALTER TABLE Invoice    ADD CONSTRAINT FK_Invoice_Table FOREIGN KEY ( tab_id ) REFERENCES Dining_Table( tab_id );
ALTER TABLE Food_Order ADD CONSTRAINT FK_Order_Invoice FOREIGN KEY ( inv_id ) REFERENCES Invoice( inv_id );
ALTER TABLE Food_Order ADD CONSTRAINT FK_Order_Product FOREIGN KEY ( prod_id ) REFERENCES Product( prod_id );