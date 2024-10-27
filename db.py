from flask import g, current_app
import sqlite3
import click
from werkzeug.security import generate_password_hash
import os
import json
import io


def get_db():
	if "db" not in g:
			g.db = sqlite3.connect(
				current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
			)
			g.db.row_factory = sqlite3.Row
	return g.db


def close_db(e=None):
	db = g.pop("db", None)
	if db is not None:
			db.close()


def add_new_team(db, team_name, city, year_formed):
	error = None
	try:
		db.execute(
				"INSERT INTO teams"
				"(team_name, city, year_formed)"
				"VALUES (?, ?, ?);",
				(team_name, city, year_formed)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_user(db, username, password):
	error = None
	try:
		hashed_psw = generate_password_hash(password)
		db.execute(
				"INSERT INTO users"
				"(username, password)"
				"VALUES (?, ?);",
				(username, hashed_psw)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_award(db, award_name, season_id):
	error = None
	try:
		db.execute(
				"INSERT INTO awards"
				"(award_name, season_id)"
				"VALUES (?, ?);",
				(award_name, season_id)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_game(db, game_date, location):
	error = None
	if "." in game_date:
		game_date = game_date.split(".")
		temp = game_date[0]
		game_date[0] = game_date[2]
		game_date[2] = temp
		game_date = "-".join(game_date)

	try:
		db.execute(
				"INSERT INTO games"
				"(game_date, location)"
				"VALUES (?, ?);",
				(game_date, location)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}

	
def add_new_judge(db, name, experience_years):
	error = None
	try:
		db.execute(
				"INSERT INTO judges"
				"(name, experience_years)"
				"VALUES (?, ?);",
				(name, experience_years)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_match(db, game_id, team1_id, team2_id, winner_team_id):
	error = None
	try:
		db.execute(
				"INSERT INTO matches"
				"(game_id, team1_id, team2_id, winner_team_id)"
				"VALUES (?, ?, ?, ?);",
				(game_id, team1_id, team2_id, winner_team_id)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_participants(db, name, age, photo, team_id):
	error = None
	try:
		photo_path = "/assets/sportsmen/football/" + photo
		db.execute(
				"INSERT INTO participants"
				"(name, age, photo, team_id)"
				"VALUES (?, ?, ?, ?);",
				(name, age, photo_path, team_id)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_result(db, game_id, team_id, score):
	error = None
	try:
		db.execute(
				"INSERT INTO results"
				"(game_id, team_id, score)"
				"VALUES (?, ?, ?);",
				(game_id, team_id, score)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_score(db, game_id, judge_id, team_id, score):
	error = None
	try:
		db.execute(
				"INSERT INTO scores"
				"(game_id, judge_id, team_id, score)"
				"VALUES (?, ?, ?, ?);",
				(game_id, judge_id, team_id, score)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_season(db, year, champion_team_id):
	error = None
	try:
		db.execute(
				"INSERT INTO seasons"
				"(year, champion_team_id)"
				"VALUES (?, ?);",
				(year, champion_team_id)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_team_history(db, team_id, event_date, event_description):
	error = None
	try:
		db.execute(
				"INSERT INTO team_history"
				"(team_id, event_date, event_description)"
				"VALUES (?, ?, ?);",
				(team_id, event_date, event_description)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_team_statistics(db, team_id, total_games, total_wins, total_losses):
	error = None
	try:
		db.execute(
				"INSERT INTO team_statistics"
				"(team_id, total_games, total_wins, total_losses)"
				"VALUES (?, ?, ?, ?);",
				(team_id, total_games, total_wins, total_losses)
			)
		db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def remove_team(team_id):
	db = get_db()
	try:
		db.execute("DELETE FROM teams WHERE team_id = ?;", (team_id,))
		db.commit()
	except db.IntegrityError as e:
		return {'status': e}
	return {'status': 'success'}


def remove_game(game_id):
	db = get_db()
	try:
		db.execute("DELETE FROM games WHERE game_id = ?;", (game_id,))
		db.commit()
	except db.IntegrityError as e:
		return {'status': e}
	return {'status': 'success'}


def update_team(team_id, data):
	db = get_db()
	try:
		db.execute("UPDATE teams SET team_name = ?, city = ?, year_formed = ? WHERE team_id = ?;", (data['new_name'], data['new_city'], data['new_year'], team_id))
		db.commit()
	except db.IntegrityError as e:
		return {'status': e}
	return {'status': 'success'}


def update_game(game_id, data):
	game_date = data['game_date']
	if "." in game_date:
		game_date = game_date.split(".")
		temp = game_date[0]
		game_date[0] = game_date[2]
		game_date[2] = temp
		game_date = "-".join(game_date)
	print(game_date)
	db = get_db()
	try:
		db.execute("UPDATE games SET game_date = ?, location = ? WHERE game_id = ?;", (game_date, data['location'], game_id))
		db.commit()
	except db.IntegrityError as e:
		return {'status': e}
	return {'status': 'success'}


def insert_data():

	db = sqlite3.connect(
			"hackathon.db", detect_types=sqlite3.PARSE_DECLTYPES
		)

	path = os.getcwd() + "/static/db_data/"

	# администратор
	add_new_user(db, "admin", "admin")

	# команды
	with open(path+'teams.json') as f:
		data = json.load(f)['teams']
		for e in data:
			add_new_team(db, e['team_name'], e['city'], e['year_formed'])

	# награды
	with open(path+'awards.json') as f:
		data = json.load(f)['awards']
		for e in data:
			add_new_award(db, e['award_name'], e['season_id'])
	# игры
	with open(path+'games.json') as f:
		data = json.load(f)['games']
		for e in data:
			add_new_game(db, e['game_date'], e['location'])

	# судьи
	with open(path+'judges.json') as f:
		data = json.load(f)['judges']
		for e in data:
			add_new_judge(db, e['name'], e['experience_years'])

	# матчи
	with open(path+'matches.json') as f:
		data = json.load(f)['matches']
		for e in data:
			add_new_match(db, e['game_id'], e['team1_id'], e['team2_id'], e['winner_team_id'])

	# члены команды
	with open(path+'participants.json') as f:
		data = json.load(f)['participants']
		for e in data:
			add_new_participants(db, e['name'], e['age'], e['photo'], e['team_id'])

	# результаты
	with open(path+'results.json') as f:
		data = json.load(f)['results']
		for e in data:
			add_new_result(db, e['game_id'], e['team_id'], e['score'])

	# оценки
	with open(path+'scores.json') as f:
		data = json.load(f)['scores']
		for e in data:
			add_new_score(db, e['game_id'], e['judge_id'], e['team_id'], e['score'])

	# сезоны
	with open(path+'seasons.json') as f:
		data = json.load(f)['seasons']
		for e in data:
			add_new_season(db, e['year'], e['champion_team_id'])

	# события
	with open(path+'team_history.json') as f:
		data = json.load(f)['team_history']
		for e in data:
			add_new_team_history(db, e['team_id'], e['event_date'], e['event_description'])

	# статистика
	with open(path+'team_statistics.json') as f:
		data = json.load(f)['team_statistics']
		for e in data:
			add_new_team_statistics(db, e['team_id'], e['total_games'], e['total_wins'], e['total_losses'])


def get_all_teams():
	db = get_db()
	return db.execute("SELECT team_id, team_name, city, year_formed FROM teams").fetchall()


def get_all_games():
	db = get_db()
	return db.execute("SELECT game_id, game_date, location FROM games").fetchall()


def get_all_matches():
	db = get_db()
	return db.execute("SELECT match_id, game_id, team1_id, team2_id, winner_team_id FROM matches").fetchall()


def get_all_awards():
	db = get_db()
	return db.execute("SELECT award_id, award_name, season_id FROM awards").fetchall()


def get_all_events():
	db = get_db()
	return db.execute("SELECT history_id, team_id, event_date, event_description FROM team_history").fetchall()


def get_matches_by_game_id(game_id):
	db = get_db()
	return db.execute("SELECT match_id, game_id, team1_id, team2_id, winner_team_id FROM matches WHERE game_id = ?", (game_id,)).fetchall()


def get_game_by_id(game_id):
	db = get_db()
	return db.execute("SELECT game_id, game_date, location FROM games WHERE game_id = ?", (game_id,)).fetchall()[0]


def get_match_by_id(match_id):
	db = get_db()
	return db.execute("SELECT game_id, team1_id, team2_id, winner_team_id FROM matches WHERE match_id = ?", (match_id,)).fetchall()[0]


def get_match_results(match_id):
	db = get_db()
	match = get_match_by_id(match_id)
	team1 = get_team_by_id(match['team1_id'])
	team2 = get_team_by_id(match['team2_id'])
	winner_team = get_team_by_id(match['winner_team_id'])
	return {"team1": team1, "team2": team2, "winner_team": winner_team}


def get_season_by_id(season_id):
	db = get_db()
	return db.execute("SELECT year, champion_team_id FROM seasons WHERE season_id = ?", (season_id,)).fetchall()[0]


def get_team_by_id(team_id):
	db = get_db()
	return db.execute("SELECT team_name, city, year_formed FROM teams WHERE team_id = ?", (team_id,)).fetchall()[0]


def get_team_statistics(team_id):
	db = get_db()
	return db.execute("SELECT total_games, total_wins, total_losses FROM team_statistics WHERE team_id = ?", (team_id,)).fetchall()[0]


def get_team_participants(team_id):
	db = get_db()
	return db.execute("SELECT name, age, photo FROM participants WHERE team_id = ?", (team_id,)).fetchall()


def get_team_champion_season_years(team_id):
	db = get_db()
	return db.execute("SELECT year FROM seasons WHERE champion_team_id = ?", (team_id,)).fetchall()[0]


def get_team_events(team_id):
	db = get_db()
	return db.execute("SELECT event_date, event_description FROM team_history WHERE team_id = ?", (team_id,)).fetchall()

def get_user_by_id(user_id):
	db = get_db()
	return db.execute("SELECT username, password FROM users WHERE id = ?", (user_id,)).fetchone()


def get_user_by_name(username):
	db = get_db()
	return db.execute("SELECT id, username, password FROM users WHERE username = ?", (username,)).fetchone()


def init_db():
	db = sqlite3.connect(
				"hackathon.db", detect_types=sqlite3.PARSE_DECLTYPES
			)
	with open("./hackathon.sql") as f:
		db.executescript(f.read())
		print("Database created")
		insert_data()
		print("Data inserted")


def init_app(app):
	app.teardown_appcontext(close_db)
	init_db()
