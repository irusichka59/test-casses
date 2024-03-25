import requests
import json


# Функція для отримання даних про корабель Millennium Falcon та його пілотів
def get_millennium_falcon_data():
    # Запит до API для отримання даних про всі зіркові кораблі
    url = "https://swapi.dev/api/starships/"
    response = requests.get(url)
    data = response.json()

    # Пошук корабля Millennium Falcon
    for starship in data["results"]:
        if starship["name"] == "Millennium Falcon":
            # Інформація про корабель
            millennium_falcon_info = {
                "name": starship["name"],
                "max_speed": starship["max_atmosphering_speed"],
                "class": starship["starship_class"],
                "pilots": []
            }

            # Отримання даних про пілотів Millennium Falcon
            for pilot_url in starship["pilots"]:
                pilot_response = requests.get(pilot_url)
                pilot_data = pilot_response.json()
                pilot_info = {
                    "name": pilot_data["name"],
                    "height": pilot_data["height"],
                    "weight": pilot_data["mass"],
                    "homeworld_name": "",
                    "homeworld_url": pilot_data["homeworld"]
                }

                # Отримання назви рідної планети пілота
                homeworld_response = requests.get(pilot_data["homeworld"])
                homeworld_data = homeworld_response.json()
                pilot_info["homeworld_name"] = homeworld_data["name"]

                # Додавання інформації про пілота до корабля Millennium Falcon
                millennium_falcon_info["pilots"].append(pilot_info)

            return millennium_falcon_info


# Функція для збереження даних у JSON-файл
def save_to_json(data, filename):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


# Отримання даних про Millennium Falcon та збереження їх у JSON-файл
millennium_falcon_data = get_millennium_falcon_data()
if millennium_falcon_data:
    save_to_json(millennium_falcon_data, "millennium_falcon.json")
    print("Дані про Millennium Falcon та його пілотів успішно збережені у файлі millennium_falcon.json.")
else:
    print("Не вдалося знайти дані про Millennium Falcon.")


