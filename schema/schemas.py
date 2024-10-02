from models.cities import City


def individual_serial(city: City) -> dict:
    return {
        "id": str(city["_id"]),
        "name": city["name"],
        "country": city["country"],
        "population": city["population"],
        "area_km2": city["area_km2"],
        "coordinates": {
            "latitude": city["coordinates"]["latitude"],
            "longitude": city["coordinates"]["longitude"],
        },
        "famous_landmarks": city["famous_landmarks"],
    }


def list_serial(cities: list) -> list:
    return [individual_serial(city) for city in cities]
