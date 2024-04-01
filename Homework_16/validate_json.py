import json
from Homework_16.Schema.pets_schema import PetsSchema

from marshmallow import ValidationError


def validate_json(json_file):
    # Завантаження JSON-даних з файлу
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Виконання валідації JSON-даних
    try:
        result = PetsSchema(many=True).load(data)
        print("Дані є відповідними схемі.")
        return result
    except ValidationError as e:
        print("Помилка валідації:", e)


if __name__ == '__main__':
    validate_json('my_json_file.json')

