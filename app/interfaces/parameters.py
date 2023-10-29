from abc import ABC, abstractmethod


class IParameters(ABC):
    @property
    @abstractmethod
    def parameters(self):
        pass

