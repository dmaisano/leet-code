CALL drop_all_tables ();

CREATE TABLE If NOT EXISTS Employee (
  id int,
  name varchar(255),
  department varchar(255),
  managerId int
);

INSERT INTO
  Employee (id, name, department, managerId)
VALUES
  ('101', 'John', 'A', NULL);

INSERT INTO
  Employee (id, name, department, managerId)
VALUES
  ('102', 'Dan', 'A', '101');

INSERT INTO
  Employee (id, name, department, managerId)
VALUES
  ('103', 'James', 'A', '101');

INSERT INTO
  Employee (id, name, department, managerId)
VALUES
  ('104', 'Amy', 'A', '101');

INSERT INTO
  Employee (id, name, department, managerId)
VALUES
  ('105', 'Anne', 'A', '101');

INSERT INTO
  Employee (id, name, department, managerId)
VALUES
  ('106', 'Ron', 'B', '101');

-- ? START SOLUTION
SELECT
  e1.name
FROM
  Employee e1
  JOIN Employee e2 ON e1.id = e2.managerId
GROUP BY
  e1.id,
  e1.name
HAVING
  COUNT(e2.id) >= 5;

-- ? END SOLUTION
