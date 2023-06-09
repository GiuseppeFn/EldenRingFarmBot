from abc import ABC, abstractmethod
from ctypes import windll
windll.kernel32.SetDllDirectoryW(None)


WALK_TIMEOUTS = [3, 0.5, 2.3, 3]
class Emulator(ABC):
    @abstractmethod
    def walk(self, x: int, y: int, interval: float) -> None:
        ...
    
    def ability(self, key: str) -> None:
        ...
    
    def back_to_grace(self, timeout: float) -> None:
        ...

from src.emulators.joystick import Joystick # Used by main for importing those without importing each file
from src.emulators.keyboard import Keyboard # Used by main for importing those without importing each file