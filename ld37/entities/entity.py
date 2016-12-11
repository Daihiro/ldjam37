import pygame
from ld37.entities.component import *

class Entity:
    def __init__(self, entity_id, components):
        self.entity_id = entity_id
        self.components = components
        self.setup()
        self.is_current_player_controllable = False
        self.is_displayable = False
        self.is_collidable = False

    def setup(self):
        return

    def update(self, game_time):
        for component in self.components:
            component.update(self, game_time)

def create_playable_character(entity_id, start_pos):
    e = Entity(entity_id, [ManualCharacterInputComponent(), MovementComponent(), CollisionComponent()])
    e.done = False
    e.rect = pygame.rect.Rect(start_pos[0], start_pos[1], 30, 30)
    e.image = pygame.Surface((30, 30))
    e.speed = 200 #200 pixels/second
    e.is_displayable = True
    e.is_collidable = True
    return e

def create_static_collidable(entity_id, start_pos):
    e = Entity(entity_id, [])
    e.rect = pygame.rect.Rect(start_pos[0], start_pos[1], 30, 30)
    e.image = pygame.Surface((30, 30))
    e.speed = 0
    e.is_displayable = True
    e.is_collidable = True
    return e
