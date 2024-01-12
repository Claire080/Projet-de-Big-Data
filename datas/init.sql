-- init.sql
SELECT 'Creating database...' as status;
DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'sentiment_analysis') THEN
        CREATE DATABASE sentiment_analysis;
    END IF;
END $$;

\c sentiment_analysis;

CREATE TABLE sentiment_data (
    id SERIAL PRIMARY KEY,
    symbols VARCHAR(255),
    company_names VARCHAR(255), 
    commentaires TEXT
);

CREATE TABLE sentiment_data_analyzed (
    id SERIAL PRIMARY KEY,
    symbols VARCHAR(255),
    company_names VARCHAR(255),
    commentaires TEXT,
    impressions FLOAT,
    sentiment_category VARCHAR(25)
);
