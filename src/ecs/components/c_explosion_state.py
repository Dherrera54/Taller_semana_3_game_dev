from enum import Enum
import pygame
class CExplosionState:
    def __init__(self) -> None:
        self.state = ExplosionState.START
class ExplosionState(Enum):
    START = 0
    END = 1