"""Da EntityManager class"""

from player import Player
from bullet import Bullet

class EntityManager:
    """Stores all entitites and allows for mass updating/drawing"""
    entities = list()
    bullets = list()

    player = None

    is_updating = False
    added_entities = list()

    @classmethod
    def count(cls):
        """Returns current number of entities"""
        return len(cls.entities)

    @classmethod
    def add(cls, entity):
        """Adds an entity to the entity list(s), eventually.
        If currently iterating through entity list then add it to
        pending entites."""
        if cls.is_updating:
            cls.added_entities.append(entity)
        else:
            cls.add_entity(entity)

    @classmethod
    def add_entity(cls, entity):
        """Adds entity the entity list as well as any other
        relevant lists"""
        cls.entities.append(entity)

        if isinstance(entity, Bullet):
            cls.bullets.append(entity)
        elif isinstance(entity, Player):
            # This overwrites the player
            cls.player = entity
        else:
            # who cares
            pass
            #raise Exception("Entity of unknown type added\n"
                #f"Entity is {entity}, type is {type(entity)}")

    @classmethod
    def update(cls):
        """Updates all entities at once and removes any expired entities"""
        cls.is_updating = True

        # Handle collisions

        for entity in cls.entities:
            entity.update()

        cls.is_updating = False

        for entity in cls.added_entities:
            cls.add_entity(entity)

        cls.added_entities.clear()

        # Remove expired entities
        cls.entities = list(filter(lambda e: not e.is_expired, cls.entities))

    @classmethod
    def draw(cls, screen):
        """Draws all entities at once"""
        for entity in cls.entities:
            entity.draw(screen)

