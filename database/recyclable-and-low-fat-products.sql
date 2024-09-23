CALL drop_all_tables ();

CREATE TABLE If NOT EXISTS Products (
  product_id int,
  low_fats ENUM ('Y', 'N'),
  recyclable ENUM ('Y', 'N')
);

INSERT INTO
  Products (product_id, low_fats, recyclable)
VALUES
  ('0', 'Y', 'N');

INSERT INTO
  Products (product_id, low_fats, recyclable)
VALUES
  ('1', 'Y', 'Y');

INSERT INTO
  Products (product_id, low_fats, recyclable)
VALUES
  ('2', 'N', 'Y');

INSERT INTO
  Products (product_id, low_fats, recyclable)
VALUES
  ('3', 'Y', 'Y');

INSERT INTO
  Products (product_id, low_fats, recyclable)
VALUES
  ('4', 'N', 'N');

-- ? START SOLUTION
SELECT
  p.product_id
FROM
  Products p
WHERE
  p.low_fats = 'Y'
  AND p.recyclable = 'Y';

-- ? END SOLUTION
