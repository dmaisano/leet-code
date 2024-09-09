-- ? This function will drop all tables in the current schema

DELIMITER $$

CREATE PROCEDURE drop_all_tables()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE tbl_name VARCHAR(255);

    -- Declare a cursor to get the list of tables in the current schema
    DECLARE cur CURSOR FOR
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = DATABASE();

    -- Declare a handler to set 'done' when there are no more rows
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Disable foreign key checks
    SET FOREIGN_KEY_CHECKS = 0;

    -- Open the cursor
    OPEN cur;

    -- Loop through all the tables and drop each one
    read_loop: LOOP
        FETCH cur INTO tbl_name;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Dynamically generate and execute the DROP TABLE statement
        SET @drop_query = CONCAT(
            'DROP TABLE IF EXISTS `', DATABASE(), '`.`', tbl_name, '`;'
        );
        PREPARE stmt FROM @drop_query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    -- Close the cursor
    CLOSE cur;

    -- Re-enable foreign key checks
    SET FOREIGN_KEY_CHECKS = 1;
END $$

DELIMITER ;
