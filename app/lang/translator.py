from typing import Any
import json


class Translator:
    _instances: dict[str, 'Translator'] = {}

    def __new__(cls, lang: str) -> 'Translator':
        if lang not in cls._instances:
            cls._instances[lang] = super(Translator, cls).__new__(cls)
        return cls._instances[lang]

    def __init__(self, lang: str):
        self.lang = lang

    def get_translate(self, page: str, **kwargs: dict[str, Any]) -> dict[str, str]:
        with open(f"app/lang/{self.lang}/{page}.json", encoding="utf-8") as file:
            translation = json.load(file)
        if kwargs.keys():
            for key in translation:
                translation[key] = translation[key].format(**kwargs)
        return translation
