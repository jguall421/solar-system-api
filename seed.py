from app import create_app, db
from app.models.planet import Planet
from dotenv import load_dotenv
load_dotenv()

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(name="Mercury", description="The smallest planet, closest to the Sun.", size="4,879 km diameter")),
    db.session.add(Planet(name="Venus", description="Hottest planet with a thick, toxic atmosphere.", size="12,104 km diameter")),
    db.session.add(Planet(name="Earth", description="Our home planet with abundant life and water.", size="12,742 km diameter")),
    db.session.add(Planet(name="Mars", description="The red planet known for its iron oxide dust.", size="6,779 km diameter")),
    db.session.add(Planet(name="Jupiter", description="Largest planet, a gas giant with 79 moons.", size="139,820 km diameter")),
    db.session.add(Planet(name="Saturn", description="Famous for its prominent ring system.", size="116,460 km diameter")),
    db.session.add(Planet(name="Uranus", description="An ice giant that rotates on its side.", size="50,724 km diameter")),
    db.session.add(Planet(name="Neptune", description="Deep blue planet with supersonic winds.", size="49,244 km diameter")),
    db.session.add(Planet(name="Pluto", description="Dwarf planet in the Kuiper Belt.", size="2,377 km diameter")),
    db.session.commit()