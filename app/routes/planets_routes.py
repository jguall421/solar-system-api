from flask import Blueprint, abort, make_response
# from .models.planets import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planet")

# @planets_bp.get("")
# def get_all_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(
#             {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "size": planet.size,
#             }
#         )
#     return planets_response

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
