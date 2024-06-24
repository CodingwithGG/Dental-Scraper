from abc import abstractmethod, ABC


class NotifierInterface(ABC):

    @abstractmethod
    def notify(self, message: str):
        """"""


class PrintNotifier:

    def notify(self, message: str):
        print(message)

# Any other notifier can be added in future based on requirements
