CALL drop_all_tables ();
CREATE TABLE If NOT EXISTS cinema (
    id int,
    movie varchar(255),
    description varchar(255),
    rating float(2, 1)
);
INSERT INTO
    cinema (id, movie, description, rating)
VALUES
    ('1', 'War', 'great 3D', '8.9');
INSERT INTO
    cinema (id, movie, description, rating)
VALUES
    ('2', 'Science', 'fiction', '8.5');
INSERT INTO
    cinema (id, movie, description, rating)
VALUES
    ('3', 'irish', 'boring', '6.2');
INSERT INTO
    cinema (id, movie, description, rating)
VALUES
    ('4', 'Ice song', 'Fantacy', '8.6');
INSERT INTO
    cinema (id, movie, description, rating)
VALUES
    ('5', 'House card', 'Interesting', '9.1');

-- ? START SOLUTION
SELECT
    *
FROM
    cinema c
WHERE
    (c.id % 2) != 0
    AND c.description != "boring"
ORDER BY
    c.rating DESC;
-- ? END SOLUTION
