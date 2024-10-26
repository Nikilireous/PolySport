import json
import os

with open("app_config.json") as file:
	CONFIG_FILE = json.load(file)


class Config(object):
	global CONFIG_FILE
	SECRET_KEY = CONFIG_FILE["SECRET_KEY"]
	DATABASE = os.path.join(os.getcwd(), CONFIG_FILE["DATABASE"])
	