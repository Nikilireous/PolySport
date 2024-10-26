-- Таблица команд
CREATE TABLE teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    year_formed INT
);

-- Таблица участников
CREATE TABLE participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица игр
CREATE TABLE games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    game_date DATE NOT NULL,
    location VARCHAR(100) NOT NULL
);

-- Таблица результатов
CREATE TABLE results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    team_id INT,
    score INT,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица судей
CREATE TABLE judges (
    judge_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    experience_years INT
);

-- Таблица оценок
CREATE TABLE scores (
    score_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    judge_id INT,
    team_id INT,
    score INT,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (judge_id) REFERENCES judges(judge_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица сезонов
CREATE TABLE seasons (
    season_id INT AUTO_INCREMENT PRIMARY KEY,
    year INT NOT NULL,
    champion_team_id INT,
    FOREIGN KEY (champion_team_id) REFERENCES teams(team_id) ON DELETE SET NULL
);

-- Таблица наград
CREATE TABLE awards (
    award_id INT AUTO_INCREMENT PRIMARY KEY,
    award_name VARCHAR(100) NOT NULL,
    season_id INT,
    FOREIGN KEY (season_id) REFERENCES seasons(season_id) ON DELETE SET NULL
);

-- Таблица матчей
CREATE TABLE matches (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    team1_id INT,
    team2_id INT,
    winner_team_id INT,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (team1_id) REFERENCES teams(team_id),
    FOREIGN KEY (team2_id) REFERENCES teams(team_id),
    FOREIGN KEY (winner_team_id) REFERENCES teams(team_id)
);

-- Таблица статистики команд
CREATE TABLE team_statistics (
    stat_id INT AUTO_INCREMENT PRIMARY KEY,
    team_id INT,
    total_games INT DEFAULT 0,
    total_wins INT DEFAULT 0,
    total_losses INT DEFAULT 0,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица истории команд
CREATE TABLE team_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    team_id INT,
    event_date DATE NOT NULL,
    event_description TEXT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица пользователей с возможностью редактирования
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,
);
