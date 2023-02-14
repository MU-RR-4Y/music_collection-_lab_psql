DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS album;

CREATE TABLE artists(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);

CREATE TABLE albums(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    songs INT,
    artist_id INT NOT NULL REFERENCES artists(id)
)