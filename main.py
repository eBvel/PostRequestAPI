from data import GoogleMapConfig
from file_manager import FileManager
from service import GoogleMapService
from tests import TestGoogleMapAPI


def main():
    print("\nSTART TESTING")

    file_path = "list_of_place_id.txt"
    api_service = GoogleMapService(GoogleMapConfig())
    api_test = TestGoogleMapAPI(api_service)

    # Проверяем создание (POST) одной локации, и поиск (GET) данной локации.
    place_id = api_test.test_create_location(expected_status_code=200)
    api_test.test_find_location(place_id, expected_status_code=200)

    # Проверяем, что получим 5 place_id, если создаем 5 локаций.
    place_id_list = api_test.test_create_multiple_locations(count=5)
    # Записываем полученный place_id_list в файл.
    FileManager.write_list(file_path, place_id_list)
    print(f"\nPlace_id list: {place_id_list}")
    # Считываем из файла ранее записанный place_id_list.
    recorded_place_id_list = FileManager.read_line_by_line(file_path)
    print(f"Recorded place_id list: {recorded_place_id_list}")
    # Проверяем, что список записался корректно, без артифактов.
    api_test.test_recorded_place_id_list(place_id_list, recorded_place_id_list)

    print("\nTEST PASSED")


if __name__ == "__main__":
    main()