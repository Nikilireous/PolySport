from flask import Flask
import routing, auth, db, config_module


def create_app():
	app = Flask(__name__)
	app.config.from_object(config_module.Config())

	app.register_blueprint(auth.bp)
	app.register_blueprint(routing.bp)

	app.add_url_rule("/", endpoint="index")

	db.init_app(app)
	
	return app