import pygame
from ld37.common.constants import Colors
from ld37.entities.component import *

class Entity:
    def __init__(self, entity_id, components):
        self.entity_id = entity_id
        self.components = components
        self.setup()
        self.is_current_player_controllable = False
        self.is_displayable = False
        self.is_collidable = False
        self.speed = 0

    def setup(self):
        return

    def update(self, game_time):
        for component in self.components:
            component.update(self, game_time)

def create_playable_character(entity_id, start_pos, size, starting_image_name):
    e = Entity(entity_id, [ManualCharacterInputComponent(), MovementComponent(), SpriteAnimationComponent()])
    e.done = False
    e.rect = pygame.rect.Rect(start_pos[0], start_pos[1], size[0], size[1])
    e.speed = 200 #200 pixels/second
    e.is_displayable = True
    e.is_collidable = True

    sprite_name_components = starting_image_name.split("_")
    e.sprite_name = sprite_name_components[0]
    e.sprite_direction = sprite_name_components[1]
    e.sprite_step = sprite_name_components[2]
    e.time_since_last_step = 0

    return e

def create_static_object(entity_id, start_pos, size, img_name, is_displayable, is_collidable):
    e = Entity(entity_id, [StaticObjectAnimationComponent()] if img_name != "" else [])
    e.rect = pygame.rect.Rect(start_pos[0], start_pos[1], size[0], size[1])
    e.image = pygame.Surface(size)
    e.img_name = img_name
    e.is_displayable = is_displayable
    e.is_collidable = is_collidable
    return e

def trigger_rect(entity_id, start_pos, size, triggers):
    e = Entity(entity_id, [])
    e.rect = pygame.rect.Rect(start_pos[0], start_pos[1], size[0], size[1])
