DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;


CREATE TABLE artists(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);

CREATE TABLE albums(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    songs INT,
    genre VARCHAR(255),
    artist_id INT NOT NULL REFERENCES artists(id)
);
