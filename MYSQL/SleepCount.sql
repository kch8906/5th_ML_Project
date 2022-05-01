CREATE SCHEMA ml_db;
CREATE TABLE predict_sleeping(
        LABEL VARCHAR(10) NOT NULL,
        TOTAL_SLEEP INT(10) NOT NULL,
        REGISTER_DATE TIMESTAMP NOTN NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(LABEL)
) charset='utf8';

SELECT * FROM predict_sleeping;
TRUNCATE predict_sleeping;

DROP TABLE predict_sleeping;




