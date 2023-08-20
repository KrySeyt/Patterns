from abc import ABC, abstractmethod


# Builder
class Encoder(ABC):
    @abstractmethod
    def encode(self, text: str) -> str:
        raise NotImplementedError


class JSONEncoder(Encoder):
    def encode(self, text: str) -> str:
        return "JSON encoded"


class BinaryEncoder(Encoder):
    def encode(self, text: str) -> str:
        return "Binary encoded"


class TextSaver(ABC):
    @abstractmethod
    def save(self, text: "Text") -> None:
        raise NotImplementedError


class DBTextSaver(TextSaver):
    def __init__(self) -> None:
        self._encoder = BinaryEncoder()

    def save(self, text: "Text") -> None:
        print(f"\"{text.encode(self._encoder)}\" saved to DB")


# Builder Director
class Text:
    def __init__(self, text: str) -> None:
        self._text = text

    def get_text(self) -> str:
        return self._text

    def encode(self, encoder: Encoder) -> str:
        return encoder.encode(self._text)

    def save(self, saver: TextSaver) -> None:
        saver.save(self)


def main() -> None:
    text = Text("Some info")
    saver = DBTextSaver()
    text.save(saver)


if __name__ == "__main__":
    main()
