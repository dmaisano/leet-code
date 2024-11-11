CALL drop_all_tables ();

CREATE TABLE If NOT EXISTS Person (Id int, Email varchar(255));

INSERT INTO
  Person (id, email)
VALUES
  ('1', 'john@example.com');

INSERT INTO
  Person (id, email)
VALUES
  ('2', 'bob@example.com');

INSERT INTO
  Person (id, email)
VALUES
  ('3', 'john@example.com');

DELETE p1
FROM
  Person p1
  JOIN Person p2 ON p1.email = p2.email
  AND p1.id > p2.id;
