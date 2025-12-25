from data import GoogleMapConfig
from file_manager import FileManager
from service import GoogleMapService
from tests import TestGoogleMapAPI


def main():
    print("\nSTART TESTING\n")

    file_path = "list_of_place_id.txt"
    api_service = GoogleMapService(GoogleMapConfig())
    api_test = TestGoogleMapAPI(api_service)

    """
    Выполняем POST-тест на запись локации 5 раз. Записываем place_id локации 
    в переменную file_data. Значенеие переменной записываем в файл 
    list_of_place_id.
    """
    file_data = ""
    for i in range(5):
        file_data += api_test.test_create_location(200) + "\n"
    FileManager.write(file_path, file_data)

    """
    Считываем значение список place_id из файла list_of_place_id.
    Выполняем GET-тест для поиска локаций по идентификатору(place_id).
    """
    list_of_place_id = FileManager.read_line_by_line(file_path)
    for place_id in list_of_place_id:
        api_test.test_find_location(place_id, 200)

    print("\nTEST PASSED")


if __name__ == "__main__":
    main()