from ..db import db
from sqlalchemy.orm import Mapped, mapped_column

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    size: Mapped[str]

    def to_dict(self):
        return{
            "name":self.name,
            "description":self.description,
            "size":self.size
        }

    @classmethod
    def from_dict(cls, planet_data):
        return cls(name=planet_data["name"], 
                   description=planet_data["description"],
                   size=planet_data["size"])



# class Planet:
#     def __init__(self, id, name, description, size):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.size = size

# planets = [
#     Planet(1, "Mars", "marty red planet", "6,779 km"),
#     Planet(2, "Jupiter", "the largest planet in our solar system", "139,820 km"),
#     Planet(3, "Saturn", "famous for its rings", "116,460 km"),

# ]
