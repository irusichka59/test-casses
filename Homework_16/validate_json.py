import json
from Homework_16.Schema.pets_schema import PetsSchema

from marshmallow import ValidationError


def validate_json_from_file(json_file):
    # Завантаження JSON-даних з файлу
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Виконання валідації JSON-даних
    try:
        pets = PetsSchema(many=True).load(data)
        print("Дані є відповідними схемі.")
        for pet in pets:
            tags = [tag['name'] for tag in pet['tags']]
            print(pet['name'], pet['category']['name'], tags)
    except ValidationError as e:
        print("Помилка валідації:", e)


if __name__ == '__main__':
    validate_json_from_file('my_json_file.json')
