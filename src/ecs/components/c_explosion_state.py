from enum import Enum
import pygame
class CExplosionState:
    def __init__(self,pos: pygame.Vector2) -> None:
        self.state = EnemyState.START
        self.pos_x=pos.x
        self.pos_y=pos.y

class EnemyState(Enum):
    START = 0
    END = 1