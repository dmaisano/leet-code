CALL drop_all_tables ();

CREATE TABLE If NOT EXISTS Employees (id int, name varchar(20));

CREATE TABLE If NOT EXISTS EmployeeUNI (id int, unique_id int);

INSERT INTO
  Employees (id, name)
VALUES
  ('1', 'Alice');

INSERT INTO
  Employees (id, name)
VALUES
  ('7', 'Bob');

INSERT INTO
  Employees (id, name)
VALUES
  ('11', 'Meir');

INSERT INTO
  Employees (id, name)
VALUES
  ('90', 'Winston');

INSERT INTO
  Employees (id, name)
VALUES
  ('3', 'Jonathan');

INSERT INTO
  EmployeeUNI (id, unique_id)
VALUES
  ('3', '1');

INSERT INTO
  EmployeeUNI (id, unique_id)
VALUES
  ('11', '2');

INSERT INTO
  EmployeeUNI (id, unique_id)
VALUES
  ('90', '3');

-- ? START SOLUTION
SELECT
  euni.unique_id,
  e.name
FROM
  Employees e
  LEFT JOIN EmployeeUNI euni ON e.id = euni.id;

-- ? END SOLUTION
