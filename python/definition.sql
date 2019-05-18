DROP TABLE IF EXISTS Sensors;

CREATE TABLE sensorValues (
	Temperature integer,
	Humidity integer,
	Light integer
);
INSERT INTO sensorValues (Temperature, Humidity, Light) VALUES (1,2,3);
