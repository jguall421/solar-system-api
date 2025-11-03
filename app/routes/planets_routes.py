from ..models.planet import Planet
from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from .routes_utilities import validate_model

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.from_dict(request_body)
    
    db.session.add(new_planet)
    db.session.commit()
    return new_planet.to_dict(), 201


@bp.get("")
def get_all_planets():
    query = db.select(Planet)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Planet.name.ilike(f"%{name_param}%"))

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    size_param = request.args.get("size")
    if size_param:
        query = query.where(Planet.size.ilike(f"%{size_param}%"))

    query = query.order_by(Planet.id)

    planets = db.session.scalars(query)

    result_list = []

    for planet in planets:
        result_list.append(
            planet.to_dict())
        
    return result_list

@bp.get("/<id>")
def get_one_planet(id):
    planet = validate_model(Planet, id)

    return planet.to_dict()


@bp.put("/<id>")
def replace_planet(id):
    planet = validate_model(Planet, id)
    
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.size = request_body["size"]
    planet.description = request_body["description"]
    
    db.session.commit()
    
    return Response(status = 204,mimetype ="application/json")

@bp.delete("/<id>")
def del_planet(id):
    planet = validate_model(Planet, id)
    
    db.session.delete(planet)
    
    db.session.commit()
    
    return Response(status = 204,mimetype ="application/json")





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
