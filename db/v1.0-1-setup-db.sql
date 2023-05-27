-- MySQL 8.0


CREATE TABLE IF NOT EXISTS jokes (
    joke_id INT NOT NULL,
    source VARCHAR(191) DEFAULT 'local',
    content TEXT DEFAULT NULL,
    created_at datetime DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at datetime DEFAULT NULL,
    PRIMARY KEY (`joke_id`, `source`)
);
