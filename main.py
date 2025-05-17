import requests

API_URL = "http://www.omdbapi.com/?apikey=505480d7&s="

while True:
    title = input("Введите название фильма (или напишите 'выход' чтобы завершить работу): ")

    if title.lower() == "выход":
        print("Завершение работы...")
        break

    response = requests.get(API_URL + title)
    response.raise_for_status()
    data = response.json()

    if data["Response"] == "True":
        for movie in data:
            print(f"Название: {movie['Title']}, Год: {movie['Year']}, Тип: {movie['Type']}")