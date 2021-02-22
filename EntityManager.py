import Entity
import Enemy
import Particle
import Bullet
import Player

class entity_manager:
    entities = list()
    enemies = list()
    bullets = list()
    players = list()
    particles = list()

    is_updating = False
    added_entities = list()

    @classmethod
    def count(cls):
        return len(cls.entities)
    
    @classmethod
    def add(cls, entity):
        if cls.is_updating:
            cls.add_entity(entity)
        else:
            cls.added_entities.append(entity)

    @classmethod
    def add_entity(cls, entity):
        cls.entities.append(entity)

        if isinstance(entity, Particle.Particle):
            cls.particles.append(entity)
        elif isinstance(entity, Bullet.bullet):
            cls.bullets.append(entity)
        elif isinstance(entity, Enemy.enemy):
            cls.enemies.append(entity)
        elif isinstance(entity, Player.Player):
            cls.players.append(entity)
        else:
            print("Error in entitymanager.py, add_entity, 'else'")

    @classmethod
    def update(cls):
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
        cls.enemies = list(filter(lambda e: not e.is_expired, cls.enemies))
        cls.bullets = list(filter(lambda e: not e.is_expired, cls.bullets))
        cls.particles = list(filter(lambda e: not e.is_expired, cls.particles))
        cls.players = list(filter(lambda e: not e.is_expired, cls.players))
    
    @classmethod
    def draw(cls, screen):
        for entity in cls.entities:
            entity.draw(screen)
