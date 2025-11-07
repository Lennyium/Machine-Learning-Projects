CREATE TABLE friends(
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');

INSERT INTO friends (id, name, birthday)
VALUES (2, 'Brian Ndirangu', '2000-05-05');

INSERT INTO friends (id, name, birthday)
VALUES (3, 'Lenny Gitau', '2001-03-05');

SELECT * FROM friends;

UPDATE friends
SET name = 'Storm'
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'brian@codecademy.com'
WHERE id = 2;

UPDATE friends
SET email = 'lenny@codecademy.com'
WHERE id = 3;

DELETE FROM friends
WHERE id = 1;

SELECT * FROM friends
