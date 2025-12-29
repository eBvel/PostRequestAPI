from file_manager import FileManager
from service import  GoogleMapService


class TestGoogleMapAPI:
    def __init__(self, service: GoogleMapService):
        self.service = service

    def _compare_status_code(
                        self,
                        result_code: int,
                        expected_code: int
                        ) -> None:
        print(f"Response status-code: {result_code}")
        assert result_code == expected_code
        print("PASSED: Status is correct!")

    def test_create_location(self, expected_status_code: int) -> str:
        print("\nSTART TEST: CREATE LOCATION")
        response = self.service.create_location()
        print(f"RESPONSE:\n{response.json()}")

        self._compare_status_code(response.status_code, expected_status_code)

        status = response.json().get("status")
        print(f"Response Status: {status}")
        assert status == "OK", "FAILED: Status is incorrect!"
        print("PASSED: Status is correct!\nEND TEST")

        return response.json().get("place_id")

    def test_find_location(
                        self,
                        place_id: str,
                        expected_status_code: int
                        ) -> None:
        print("\nSTART TEST: FIND LOCATION")

        response = self.service.find_location(place_id)
        print(f"RESPONSE:\n{response.json()}")

        self._compare_status_code(response.status_code, expected_status_code)
        print("END TEST")


    def test_create_multiple_locations(self, count: int) -> None:
        print(f"\nSTART TEST: Create multiple({count}) locations")
        list_of_place_id = list()
        for response in self.service.create_multiple_locations(count):
            list_of_place_id.append(response.json().get("place_id"))

        assert len(list_of_place_id) == count, ("FAILED: Incorrect length of "
                                                "place_id list!")
        print(f"PASSED: Length of place_id list is correctly!\nEND TEST")

    def test_record_place_id_list(self, list_length: int) -> None:
        print("\nSTART TEST: Record place_id list")
        file_path = "list_of_place_id.txt"
        
        initial_list = []
        for response in self.service.create_multiple_locations(list_length):
            initial_list.append(response.json().get('place_id'))

        FileManager.write_list(file_path, initial_list)
        recorded_list = FileManager.read_line_by_line(file_path)
        print(f"\nInitial list: {initial_list}\n"
              f"Recorded list: {recorded_list}\n")

        assert initial_list == recorded_list, ("FAILED: Incorrect "
                                               "place_id list!")
        print("PASSED: Place_id list is correctly!\nEND TEST")