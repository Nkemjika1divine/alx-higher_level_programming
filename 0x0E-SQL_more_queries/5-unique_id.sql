-- This script creates a table a gives it a default ID, but id must be unique 
CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
