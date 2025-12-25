from data import GoogleMapConfig
from service import GoogleMapService


class TestGoogleMapAPI:
    def __init__(self, service: GoogleMapService):
        self.service = service

    def _compare_status_code(self, result_code: int,
                             expected_code: int) -> None:
        try:
            print(f"Response status-code: {result_code}")
            assert result_code == expected_code
            print("PASSED: Status is correct!")
        except AssertionError:
            print("FAILED: Status is incorrect!")

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

    def test_find_location(self, place_id: str,
                           expected_status_code: int) -> None:
        print("\nSTART TEST: FIND LOCATION")

        response = self.service.find_location(place_id)
        print(f"RESPONSE:\n{response.json()}")

        self._compare_status_code(response.status_code, expected_status_code)
        print("END TEST")


if __name__ == "__main__":
    test = TestGoogleMapAPI(GoogleMapService(GoogleMapConfig()))
    id = test.test_create_location(200)
    test.test_find_location(id, 200)