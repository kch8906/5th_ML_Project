use ml_db;
CREATE SCHEMA ml_db;
DROP schema ml_db;

SELECT * FROM co_eyes_temp;
SELECT * FROM co_eyes_predictlabel;

TRUNCATE co_eyes_temp;

ALTER TABLE co_eyes_temp MODIFY COLUMN register_date timestamp not null default current_timestamp;
ALTER TABLE co_eyes_predictlabel MODIFY COLUMN register_date timestamp not null default current_timestamp;