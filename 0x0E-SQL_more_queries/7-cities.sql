-- Assuming database hbtn_0d_usa exists, create table cities with a foreign key, without failing if table exists
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCES states(id)
);
