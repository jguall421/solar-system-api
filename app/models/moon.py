from sqlalchemy.orm import Mapped, mapped_column,relationship
from ..db import db
from typing import Optional
from sqlalchemy import ForeignKey
from typing import Optional

class Moon(db.Model): #child
    name: Mapped[str]
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str]
    size: Mapped[str]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")
    
    
    def to_dict(self):
        moon_as_dict = {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "description":self.description,
            "planet":self.planet.name if self.planet_id else None
        }
        
        return moon_as_dict
    
    @classmethod
    def from_dict(cls, moon_data):
        new_moon = cls(
                       name=moon_data["name"],
                       size=moon_data["size"],
                       description=moon_data["description"],
                       planet_id=moon_data.get("planet_id", None)
                       )
        
        return new_moon