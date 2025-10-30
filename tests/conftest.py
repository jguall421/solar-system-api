import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from app.models.planet import Planet
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': os.environ.get('SQLACLCHEMY_DATABASE_URI')
    }


    app = create_app(test_config) # Create the Flask app with test config
    
    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()
    
@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_planet(app):
    new_planet = Planet(
        name="Earth",
        description="Our home planet",
        size="Medium"
    )
    db.session.add(new_planet)
    db.session.commit()
    #return new_planet