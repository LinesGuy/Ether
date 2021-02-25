"""Stores the EntityManager class"""

import player

class EntityManager:
    """Stores entity lists and allows for updating/drawing
    all entities at once."""
    entities = list()
    players = list()

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
            cls.add_entity(entity)
        else:
            cls.added_entities.append(entity)

    @classmethod
    def add_entity(cls, entity):
        """Adds entity the entity list as well as any other
        relevant lists"""
        cls.entities.append(entity)

        if isinstance(entity, player.Player):
            cls.players.append(entity)
        else:
            # This should never happen
            print("Error in entitymanager.py, add_entity, 'else'")

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
        cls.players = list(filter(lambda e: not e.is_expired, cls.players))

    @classmethod
    def draw(cls):
        """Draws all entities at once"""
        for entity in cls.entities:
            entity.draw()
