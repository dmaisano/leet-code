CALL drop_all_tables ();

CREATE TABLE If NOT EXISTS Transactions (
  id int,
  country varchar(4),
  state enum ('approved', 'declined'),
  amount int,
  trans_date date
);

INSERT INTO
  Transactions (id, country, state, amount, trans_date)
VALUES
  ('121', 'US', 'approved', '1000', '2018-12-18');

INSERT INTO
  Transactions (id, country, state, amount, trans_date)
VALUES
  ('122', 'US', 'declined', '2000', '2018-12-19');

INSERT INTO
  Transactions (id, country, state, amount, trans_date)
VALUES
  ('123', 'US', 'approved', '2000', '2019-01-01');

INSERT INTO
  Transactions (id, country, state, amount, trans_date)
VALUES
  ('124', 'DE', 'approved', '2000', '2019-01-07');

-- ? START SOLUTION
SELECT
  DATE_FORMAT (trans_date, '%Y-%m') AS MONTH,
  country,
  COUNT(*) AS trans_count,
  SUM(state = 'approved') AS approved_count,
  SUM(amount) AS trans_total_amount,
  SUM(
    CASE
      WHEN state = 'approved' THEN amount
      ELSE 0
    END
  ) AS approved_total_amount
FROM
  Transactions
GROUP BY
  DATE_FORMAT (trans_date, '%Y-%m'),
  country;

-- ? END SOLUTION
