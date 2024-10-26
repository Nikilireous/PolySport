from flask import render_template, g, Blueprint, request, url_for, redirect, flash, session, current_app, send_from_directory, abort
import auth, db
import os

bp = Blueprint('routing', __name__)


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
	print("redirect ->>>")
	return render_template("admin/admin-panel.html")


@bp.route('/football', methods=("GET", "POST"))
def football_page():
	events = db.get_all_events()
	res = {}
	for e in events:
		res[e['event_date']] = db.get_team_by_id(e['team_id'])['team_name']
	awards = db.get_all_awards()
	years = {}
	awarded_teams = {}
	for aw in awards:
		season = db.get_season_by_id(aw['season_id'])
		years[aw['award_name']] = season['year']
		awarded_teams[aw['award_name']] = db.get_team_by_id(season['champion_team_id'])['team_name']
	return render_template("public/football.html", teams=db.get_all_teams(), games=db.get_all_games(), events=events,
	 event_teams=res, awards=awards, awards_years=years, awarded_teams=awarded_teams)

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
