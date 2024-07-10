DROP TABLE IF EXISTS register;
CREATE TABLE register (
    user_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

DROP TABLE IF EXISTS reservation;
CREATE TABLE reservation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    number_of_people INTEGER NOT NULL,
    time TEXT NOT NULL,
    message TEXT,
    FOREIGN KEY (user_id) REFERENCES register(user_id)
);
