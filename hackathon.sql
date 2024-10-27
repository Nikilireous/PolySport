-- Таблица команд
CREATE TABLE IF NOT EXISTS teams (
	team_id INTEGER PRIMARY KEY AUTOINCREMENT,
	team_name VARCHAR(100) UNIQUE NOT NULL,
	city VARCHAR(100) NOT NULL,
	year_formed INT
);

-- Таблица участников
CREATE TABLE IF NOT EXISTS participants (
	participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(100) UNIQUE NOT NULL,
	photo VARCHAR(100) UNIQUE NOT NULL,
	age INT,
	team_id INT,
	FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица игр
CREATE TABLE IF NOT EXISTS games (
	game_id INTEGER PRIMARY KEY AUTOINCREMENT,
	game_date DATE NOT NULL,
	location VARCHAR(100) NOT NULL
);

-- Таблица результатов
CREATE TABLE IF NOT EXISTS results (
	result_id INTEGER PRIMARY KEY AUTOINCREMENT,
	game_id INT,
	team_id INT,
	score INT,
	FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
	FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица судей
CREATE TABLE IF NOT EXISTS judges (
	judge_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(100) UNIQUE NOT NULL,
	experience_years INT
);

-- Таблица оценок
CREATE TABLE IF NOT EXISTS scores (
	score_id INTEGER PRIMARY KEY AUTOINCREMENT,
	game_id INT,
	judge_id INT,
	team_id INT,
	score INT,
	FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
	FOREIGN KEY (judge_id) REFERENCES judges(judge_id) ON DELETE CASCADE,
	FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица сезонов
CREATE TABLE IF NOT EXISTS seasons (
	season_id INTEGER PRIMARY KEY AUTOINCREMENT,
	year INT UNIQUE NOT NULL,
	champion_team_id INT,
	FOREIGN KEY (champion_team_id) REFERENCES teams(team_id) ON DELETE SET NULL
);

-- Таблица наград
CREATE TABLE IF NOT EXISTS awards (
	award_id INTEGER PRIMARY KEY AUTOINCREMENT,
	award_name VARCHAR(100) UNIQUE NOT NULL,
	season_id INT,
	FOREIGN KEY (season_id) REFERENCES seasons(season_id) ON DELETE SET NULL
);

-- Таблица матчей
CREATE TABLE IF NOT EXISTS matches (
	match_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
CREATE TABLE IF NOT EXISTS team_statistics (
	stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
	team_id INT,
	total_games INT DEFAULT 0,
	total_wins INT DEFAULT 0,
	total_losses INT DEFAULT 0,
	FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица истории команд
CREATE TABLE IF NOT EXISTS team_history (
	history_id INTEGER PRIMARY KEY AUTOINCREMENT,
	team_id INT,
	event_date DATE UNIQUE NOT NULL,
	event_description TEXT,
	FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица пользователей с возможностью редактирования
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL
);
