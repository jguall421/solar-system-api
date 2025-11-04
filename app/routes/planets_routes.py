from ..models.planet import Planet
from ..models.moon import Moon
from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from .routes_utilities import validate_model,create_model, get_models_with_filters

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()

    return create_model(Planet, request_body)


@bp.post("/<id>/moons")
def create_moon_with_planet_id(id):
    planet = validate_model(Planet, id)

    request_body = request.get_json()
    request_body["planet_id"] = planet.id

    return create_model(Moon, request_body)

@bp.get("")
def get_all_planets():
    return get_models_with_filters(Planet, request.args)

@bp.get("/<id>")
def get_one_planet(id):
    
    planet = validate_model(Planet, id)
    return planet.to_dict()
