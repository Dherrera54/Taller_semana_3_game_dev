from enum import Enum
import pygame
class CEnemyState:
    def __init__(self,pos: pygame.Vector2) -> None:
        self.state = EnemyState.IDLE
        self.pos_x=pos.x
        self.pos_y=pos.y

class EnemyState(Enum):
    IDLE = 0
    MOVE = 1
