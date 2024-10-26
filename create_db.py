import sqlite3
import json
import os
from werkzeug.security import generate_password_hash

db = sqlite3.connect(
				"hackathon.db", detect_types=sqlite3.PARSE_DECLTYPES
			)


def create_db():
	with open("./hackathon.sql") as f:
		db.executescript(f.read())
		print("Database created")


def add_new_team(team_name, city, year_formed):
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


def add_new_user(username, password):
	error = None
	try:
			hashed_psw = generate_password_hash(password)
			db.execute(
					"INSERT INTO users"
					"(username, password)"
					"VALUES (?, ?);",
					(username, password)
				)
			db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_award(award_name, season_id):
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


def add_new_game(game_date, location):
	error = None
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

	
def add_new_judge(name, experience_years):
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


def add_new_match(game_id, team1_id, team2_id, winner_team_id):
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


def add_new_participants(name, age, team_id):
	error = None
	try:
			db.execute(
					"INSERT INTO participants"
					"(name, age, team_id)"
					"VALUES (?, ?, ?);",
					(name, age, team_id)
				)
			db.commit()
	except db.IntegrityError as e:
			error = e
	if error:
		return {'status': error}
	return {'status': 'success'}


def add_new_result(game_id, team_id, score):
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


def add_new_score(game_id, judge_id, team_id, score):
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


def add_new_season(year, champion_team_id):
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


def add_new_team_history(team_id, event_date, event_description):
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


def add_new_team_statistics(team_id, total_games, total_wins, total_losses):
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


def create_db():
	with open("./hackathon.sql") as f:
		db.executescript(f.read())
		print("Database created")
		insert_data()
		print("Data inserted")



def insert_data():
	# администратор
	add_new_user("admin", "admin")

	path = os.getcwd() + "/static/db_data/"

	# команды
	with open(path+'teams.json') as f:
		data = json.load(f)['teams']
		for e in data:
			add_new_team(e['team_name'], e['city'], e['year_formed'])

	# награды
	with open(path+'awards.json') as f:
		data = json.load(f)['awards']
		for e in data:
			add_new_award(e['award_name'], e['season_id'])
	# игры
	with open(path+'games.json') as f:
		data = json.load(f)['games']
		for e in data:
			add_new_game(e['game_date'], e['location'])

	# судьи
	with open(path+'judges.json') as f:
		data = json.load(f)['judges']
		for e in data:
			add_new_judge(e['name'], e['experience_years'])

	# матчи
	with open(path+'matches.json') as f:
		data = json.load(f)['matches']
		for e in data:
			add_new_match(e['game_id'], e['team1_id'], e['team2_id'], e['winner_team_id'])

	# члены команды
	with open(path+'participants.json') as f:
		data = json.load(f)['participants']
		for e in data:
			add_new_participants(e['name'], e['age'], e['team_id'])

	# результаты
	with open(path+'results.json') as f:
		data = json.load(f)['results']
		for e in data:
			add_new_result(e['game_id'], e['team_id'], e['score'])

	# оценки
	with open(path+'scores.json') as f:
		data = json.load(f)['scores']
		for e in data:
			add_new_score(e['game_id'], e['judge_id'], e['team_id'], e['score'])

	# сезоны
	with open(path+'seasons.json') as f:
		data = json.load(f)['seasons']
		for e in data:
			add_new_season(e['year'], e['champion_team_id'])

	# события
	with open(path+'team_history.json') as f:
		data = json.load(f)['team_history']
		for e in data:
			add_new_team_history(e['team_id'], e['event_date'], e['event_description'])

	# статистика
	with open(path+'team_statistics.json') as f:
		data = json.load(f)['team_statistics']
		for e in data:
			add_new_team_statistics(e['team_id'], e['total_games'], e['total_wins'], e['total_losses'])


def get_all_teams():
	return db.execute("SELECT team_id, team_name, city, year_formed FROM teams").fetchall()


def get_all_matches():
	return db.execute("SELECT match_id, game_id, team1_id, team2_id, winner_team_id FROM matches").fetchall()


def get_all_awards():
	return db.execute("SELECT award_id, award_name, season_id FROM awards").fetchall()


def get_all_events():
	return db.execute("SELECT history_id, team_id, event_date, event_description FROM team_history").fetchall()
