from abc import ABC, abstractmethod

class Showable(ABC):
    @property
    @abstractmethod
    def symbol(self) -> str:
        pass

class IUnit(ABC, Showable):
    @abstractmethod
    def move_to(self, x: int, y: int) -> bool:
        pass

class ILandscape(ABC, Showable):
    @abstractmethod
    def can_pass(self, unit: IUnit) -> bool:
        pass

    def apply_effect(self, unit: BaseUnit):
        pass

class INeutralObject(ABC, Showable):
    @abstractmethod
    def intract(self, unit: BaseUnit):
        pass


