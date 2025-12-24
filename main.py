import requests


class TestGoogleMapAPI:

    base_url = "https://rahulshettyacademy.com"
    key_param = "?key=qaclick123"

    def _compare_status_code(self, result_code, expected_code):
        try:
            print(f"Response status-code: {result_code}")
            assert result_code == expected_code
            print("PASSED: Status is correct!")
        except AssertionError:
            print("FAILED: Status is incorrect!")

    def test_create_new_location(self, body_json):
        post_url = self.base_url + "/maps/api/place/add/json" + self.key_param
        print(f"POST URL: {post_url}")

        response = requests.post(post_url, json=body_json)
        print(f"RESPONSE:\n{response.json()}")

        self._compare_status_code(response.status_code, 200)

        status = response.json().get("status")
        print(f"Response Status: {status}")
        assert status == "OK", "FAILED: Status is incorrect!"
        print("PASSED: Status is correct!")

        return response.json().get("place_id")

    def test_find_location_by_place_id(self, place_id):
        get_url = (self.base_url + "/maps/api/place/get/json"
                   + self.key_param + f"&place_id={place_id}")
        print(f"GET URL: {get_url}\nPlace id: {place_id}")

        response = requests.get(get_url)
        print(f"RESPONSE:\n{response.json()}")

        self._compare_status_code(response.status_code, 200)
        print("LOCATION FOUND")


def read_lines(file_path):
    with open(file_path, 'r', encoding="UTF-8") as file:
        for line in file:
            yield line

file_name = "list_of_place_id.txt"
request_body = {
    "location": {
        "lat": -38.383494,
        "lng": 33.427362
    },
    "accuracy": 50,
    "name": "Frontline house",
    "phone_number": "(+91) 983 893 3937",
    "address": "29, side layout, cohen 09",
    "types": ["shoe park","shop"],
    "website": "http://google.com",
    "language": "French-IN"
}
test_map = TestGoogleMapAPI()

result = ""
for i in range(5):
    result += f"{test_map.test_create_new_location(request_body)}\n"

with open(file_name, 'w', encoding="UTF-8") as file:
    file.write(f"{result}")

for id in read_lines(file_name):
    test_map.test_find_location_by_place_id(id.replace("\n", ""))

print("\nTEST PASSED")