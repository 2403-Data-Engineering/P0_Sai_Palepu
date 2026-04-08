from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING

from models.student import Student

if TYPE_CHECKING:
    from presentation_layer.terminal import Terminal

class Menu:
    def __init__(self, terminal: Terminal):
        self.terminal:Terminal = terminal

    @abstractmethod
    def render() -> None:
        pass


    
    