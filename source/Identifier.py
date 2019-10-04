from abc import ABC, abstractmethod


class Identifier(ABC):
    @abstractmethod
    def get_identifier(self):
        pass
