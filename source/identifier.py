from abc import ABC, abstractmethod


class Identifier(ABC):

    @classmethod
    @abstractmethod
    def identifier(cls):
        pass
