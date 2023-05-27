-- MySQL 8.0


CREATE TABLE IF NOT EXISTS jokes (
    joke_id VARCHAR(191) NOT NULL,
    source VARCHAR(191) DEFAULT 'local',
    content TEXT DEFAULT NULL,
    created_at datetime DEFAULT NOW(),
    updated_at datetime DEFAULT NOW() ON UPDATE NOW(),
    deleted_at datetime DEFAULT NULL,
    PRIMARY KEY (`joke_id`, `source`)
);
