from dataclasses import dataclass, field


@dataclass
class GoogleMapDataJSON:
    lat : float = -38.383494
    lng: float = 33.427362
    location: str = field(init=False,
                          default=f'{{"lat": {lat}, "lng": {lng}}}')
    accuracy : int = 50
    name : str = "Frontline house"
    phone_number : str = "(+91) 983 893 3937"
    address : str = "29, side layout, cohen 09"
    types: str = f'["shoe park", "shop"]'
    website : str = "http://google.com"
    language : str = "French-IN"

    def __repr__(self):
        return (f'{{\n"location": {self.location},\n'
                f'"accuracy": {self.accuracy},\n'
                f'"name": "{self.name}",\n'
                f'"phone_number": "{self.phone_number}",\n'
                f'"address": "{self.address}",\n'
                f'"types": {self.types},\n'
                f'"website": "{self.website}",\n'
                f'"language": "{self.language}"\n}}')


@dataclass
class GoogleMapConfig:
    url : str = "https://rahulshettyacademy.com"
    create_location_body : str = str(GoogleMapDataJSON())
    key_param: str = "?key=qaclick123"
    place_id_param : str = "&place_id="
    create_location_resource : str = "/maps/api/place/add/json"
    find_location_resource : str = "/maps/api/place/get/json"


class GoogleMapURLBuilder:
    def __init__(self, config: GoogleMapConfig):
        self.config = config

    def get_create_location_url(self) -> str:
        return (f"{self.config.url}"
                f"{self.config.create_location_resource}"
                f"{self.config.key_param}")

    def get_find_location_url(self) -> str:
        return (f"{self.config.url}"
                f"{self.config.find_location_resource}"
                f"{self.config.key_param}"
                f"{self.config.place_id_param}")