CALL drop_all_tables ();

CREATE TABLE If NOT EXISTS Person (
  personId int,
  firstName varchar(255),
  lastName varchar(255)
);

CREATE TABLE If NOT EXISTS Address (
  addressId int,
  personId int,
  city varchar(255),
  state varchar(255)
);

INSERT INTO
  Person (personId, lastName, firstName)
VALUES
  ('1', 'Wang', 'Allen');

INSERT INTO
  Person (personId, lastName, firstName)
VALUES
  ('2', 'Alice', 'Bob');

INSERT INTO
  Address (addressId, personId, city, state)
VALUES
  ('1', '2', 'New York City', 'New York');

INSERT INTO
  Address (addressId, personId, city, state)
VALUES
  ('2', '3', 'Leetcode', 'California');

-- ? START SOLUTION
SELECT
  FirstName,
  LastName,
  City,
  State
FROM
  Person p
  LEFT JOIN Address a ON p.PersonId = a.PersonId;

-- ? END SOLUTION
