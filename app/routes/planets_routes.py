from ..models.planet import Planet
from flask import Blueprint, abort, make_response, request
from ..db import db
# from .models.planets import planets
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    size = request_body["size"]

    new_planet = Planet(
        name=name,
        description=description,
        size=size
    )
    db.session.add(new_planet)
    db.session.commit()
    planet_response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "size": new_planet.size,
        "description": new_planet.description,
    }
    return planet_response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    result_list = []
    for planet in planets:
        result_list.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "size": planet.size,
            }
        )
    return result_list





# @planets_bp.get("")
# def get_all_planets():
#     planets_response = []
    # for planet in planets:
    #     planets_response.append(
    #         {
    #             "id": planet.id,
    #             "name": planet.name,
    #             "description": planet.description,
    #             "size": planet.size,
    #         }
    #     )
    # return planets_response

# @planets_bp.get("/<id>")
# def get_single_planet(id):
#     planet = validate_planet(id)
#     planet_dict = dict(
#         id = planet.id,
#         name =  planet.name,
#         size= planet.size,
#         description = planet.description
# )
    
#     return planet_dict
        
# def validate_planet(id):
#     try:
#         id = int(id)
#     except ValueError:
#         bad_request_response = {"message": f"Planet id({id}) is invalid."}

#         abort(make_response(bad_request_response, 400))

#     for planet in planets:
#         if planet.id == id:
#             return planet
        
#     not_found_response = {"message": f"Planet with id({id}) not found."}
#     abort(make_response(not_found_response, 404))
