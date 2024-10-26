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
def main():
	if g.is_admin:
		print('--> Redirecting to admin page')
		return render_template("admin/index.html")
	
	return render_template("public/home.html")


@bp.route('/football', methods=("GET", "POST"))
def football_page():
	return render_template("public/football.html")

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