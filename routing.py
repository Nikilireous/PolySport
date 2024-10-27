from flask import render_template, g, Blueprint, request, url_for, redirect, flash, session, current_app, send_from_directory, abort
import auth, db
import os

bp = Blueprint('routing', __name__)

def load_data():
	events = db.get_all_events()
	event_teams = {}
	for e in events:
		event_teams[e['event_date']] = db.get_team_by_id(e['team_id'])['team_name']
	awards = db.get_all_awards()
	years = {}
	awarded_teams = {}
	for aw in awards:
		season = db.get_season_by_id(aw['season_id'])
		years[aw['award_name']] = season['year']
		awarded_teams[aw['award_name']] = db.get_team_by_id(season['champion_team_id'])['team_name']
	return {"teams": db.get_all_teams(), 
				 "games": db.get_all_games(), 
				 "events": events, 
				 "event_teams": event_teams,
				 "awards": awards, "awards_years": years, "awarded_teams": awarded_teams}


""" Удаление пустых значений """
@bp.app_template_filter('whitespaces')
def remove_whitespaces(s):
	if len(s) == 1:
		return ""
	return s


@bp.route('/')
def index():
	return render_template("public/home.html")


@bp.route('/admin', methods=("GET", "POST"))
@auth.login_required
def admin_panel():
	data = load_data()
	return render_template("admin/admin-panel.html", teams=data['teams'], games=data['games'], events=data['events'],
	 event_teams=data['event_teams'], awards=data['awards'], awards_years=data['awards_years'], awarded_teams=data['awarded_teams'])


@bp.route('/football', methods=("GET", "POST"))
def football_page():
	data = load_data()
	return render_template("public/football.html", teams=data['teams'], games=data['games'], events=data['events'],
	 event_teams=data['event_teams'], awards=data['awards'], awards_years=data['awards_years'], awarded_teams=data['awarded_teams'])

@bp.route('/hockey', methods=("GET", "POST"))
def hockey_page():
	return render_template("public/hockey.html")

@bp.route('/tennis', methods=("GET", "POST"))
def tennis_page():
	return render_template("public/tennis.html")

@bp.route('/volleyball', methods=("GET", "POST"))
def volleyball_page():
	return render_template("public/volleyball.html")

@bp.route('/basketball', methods=("GET", "POST"))
def basketball_page():
	return render_template("public/basketball.html")


@bp.route('/team', methods=("GET", "POST"))
def team_page():
	team_id = request.args['team_id']
	team = db.get_team_by_id(team_id)
	statistics = db.get_team_statistics(team_id)
	champion_season_years = db.get_team_champion_season_years(team_id)
	events = db.get_team_events(team_id)
	participants = db.get_team_participants(team_id)
	print(champion_season_years)
	return render_template("public/team-page.html", 
	team=team, statistics=statistics, 
	champion_season_years=champion_season_years,
	events=events, participants=participants)


@bp.route('/game', methods=("GET", "POST"))
def game_page():
	game_id = request.args['game_id']
	matches = db.get_matches_by_game_id(game_id)
	game = db.get_game_by_id(game_id)
	res = {}
	for match in matches:
		res[match['match_id']] = db.get_match_results(match['match_id'])
	print(res)
	return render_template("public/game-page.html", 
	game=game, matches=matches, res=res)


@bp.route('/add-team', methods=("GET", "POST"))
@auth.login_required
def add_team():
	if request.method == "POST":
		print(f'--> Adding new team: {request.form}...')
		resp = db.add_new_team(db.get_db(), request.form["team_name"], request.form["city"], request.form["year_formed"])
		if resp['status'] != "success":
			flash(resp['status'])
		else:
			return redirect(url_for("routing.admin_panel"))
	return render_template("admin/add-team.html", main_page_url=request.referrer)


@bp.route('/add-game', methods=("GET", "POST"))
@auth.login_required
def add_game():
	if request.method == "POST":
		print(f'--> Adding new game: {request.form}...')
		resp = db.add_new_game(db.get_db(), request.form["game_date"], request.form["location"])
		if resp['status'] != "success":
			flash(resp['status'])
		else:
			return redirect(url_for("routing.admin_panel"))
	return render_template("admin/add-game.html", main_page_url=request.referrer)


@bp.route('/delete-team', methods=("GET", "POST"))
@auth.login_required
def delete_team():
	team_id = request.args['team_id']
	print(f'--> Deleting team with id = {team_id}')
	print(db.remove_team(team_id))
	return redirect(request.referrer)


@bp.route('/delete-game', methods=("GET", "POST"))
@auth.login_required
def delete_game():
	game_id = request.args['game_id']
	print(f'--> Deleting game with id = {game_id}')
	print(db.remove_game(game_id))
	return redirect(request.referrer)


@bp.route('/update-team', methods=("GET", "POST"))
@auth.login_required
def update_team():
	if request.method == "POST":
		data = {}
		team_id = request.args['team_id']
		print(f'--> Updating team: {request.form}...')
		data['new_name'] = request.form['team_name']
		data['new_year'] = request.form['year_formed']
		data['new_city'] = request.form['city']
		resp = db.update_team(team_id, data)
		if resp['status'] != "success":
				flash(resp['status'])
		else:
			return redirect(url_for("routing.admin_panel"))
	return render_template("admin/update-team.html", main_page_url=request.referrer)


@bp.route('/update-game', methods=("GET", "POST"))
@auth.login_required
def update_game():
	if request.method == "POST":
		data = {}
		game_id = request.args['game_id']
		print(f'--> Updating game: {request.form}...')
		data['game_date'] = request.form['game_date']
		data['location'] = request.form['location']
		resp = db.update_game(game_id, data)
		if resp['status'] != "success":
				flash(resp['status'])
		else:
			return redirect(url_for("routing.admin_panel"))
	teams = db.get_all_games()
	return render_template("admin/update-game.html", main_page_url=request.referrer, teams=teams)