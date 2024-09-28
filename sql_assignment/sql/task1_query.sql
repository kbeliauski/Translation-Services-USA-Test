-- Task 1: Retrieve department IDs where every male has given a rating strictly greater than 5.

SELECT DISTINCT department_id
FROM evaluations
WHERE department_id IS NOT NULL
AND gender = true
GROUP BY department_id
HAVING COUNT(*) = COUNT(CASE WHEN value > 5 THEN 1 END);


/*
this is the test code I used
-- Create the table with UUID stored as CHAR(36) in MySQL
CREATE TABLE evaluations (
    respondent_id CHAR(36) PRIMARY KEY,   -- UUID as a 36-character string
    department_id INT,               -- UUID as a 36-character string
    name VARCHAR(64),
    bio LONGTEXT,                         -- Use LONGTEXT for large text in MySQL
    gender BOOLEAN,                       -- BOOLEAN type for gender
    value INT
);

-- Insert sample data with auto-generated UUIDs
INSERT INTO evaluations (respondent_id, department_id, name, bio, gender, value)
VALUES
    (UUID(), 1, 'John Doe', 'John is a developer.', true, 6),
    (UUID(), 2, 'Jane Doe', 'Jane is a designer.', false, 7),
    (UUID(), 2, 'Mark Doe', 'Mark is a tester.', true, 8),
    (UUID(), 3, 'Tom Smith', 'Tom is a manager.', true, 4);

-- Query the data
SELECT * FROM evaluations;

-- Start a transaction
START TRANSACTION;

-- Test your query
SELECT department_id
FROM evaluations
WHERE gender = true
GROUP BY department_id
HAVING COUNT(*) = COUNT(CASE WHEN value > 5 THEN 1 END);

-- Rollback the transaction to undo changes
ROLLBACK;
*/ 