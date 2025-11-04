from ..models.moon import Moon
from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from .routes_utilities import validate_model, create_model, get_models_with_filters
from ..models.planet import Planet


bp = Blueprint("moons_bp", __name__, url_prefix="/moons")

@bp.post("")
def create_moon():
    request_body = request.get_json()

    return create_model(Moon, request_body)


@bp.get("")
def get_all_moons():
    
    return get_models_with_filters(Moon, request.args)


@bp.get("/<id>")
def get_one_moon(id):
    moon = validate_model(Moon, id)

    return moon.to_dict()

@bp.get("/<planet_id>/moons")
def get_moons_by_planet(planet_id):
    moon = validate_model(Planet, planet_id)
    response = [moon.to_dict() for moon in moon.planets]
    return response





# @bp.put("/<id>")
# def replace_planet(id):
#     planet = validate_model(Planet, id)
    
#     request_body = request.get_json()
#     planet.name = request_body["name"]
#     planet.size = request_body["size"]
#     planet.description = request_body["description"]
    
#     db.session.commit()
    
#     return Response(status = 204,mimetype ="application/json")

# @bp.delete("/<id>")
# def del_planet(id):
#     planet = validate_model(Planet, id)
    
#     db.session.delete(planet)
    
#     db.session.commit()
    
#     return Response(status = 204,mimetype ="application/json")







