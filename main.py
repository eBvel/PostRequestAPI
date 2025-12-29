from data import GoogleMapConfig
from service import GoogleMapService
from tests import TestGoogleMapAPI


def main():
    print("\nSTART TESTING")

    api_service = GoogleMapService(GoogleMapConfig())
    api_test = TestGoogleMapAPI(api_service)

    # Проверяем создание (POST) одной локации, и поиск (GET) данной локации.
    place_id = api_test.test_create_location(expected_status_code=200)
    api_test.test_find_location(place_id, expected_status_code=200)

    # Проверяем, что получим 5 place_id, если создаем 5 локаций.
    api_test.test_create_multiple_locations(count=5)

    # Проверяем, что список идентификаторов place_id
    # записывается и считывается корректно.
    api_test.test_record_place_id_list(list_length=5)

    print("\nTEST PASSED")


if __name__ == "__main__":
    main()