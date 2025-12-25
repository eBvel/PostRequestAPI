import requests
from requests import Response
from data import GoogleMapConfig, GoogleMapURLBuilder


class GoogleMapService:
    def __init__(self, config: GoogleMapConfig):
        self.config = config
        self.builder = GoogleMapURLBuilder(config)
        self.session = requests.Session()

    def create_location(self) -> Response:
        url = self.builder.get_create_location_url()
        print(f"POST URL: {url}")
        with self.session as session:
            response = session.post(url, self.config.create_location_body)
        return response

    def find_location(self, place_id: str) -> Response:
        url = self.builder.get_find_location_url()+place_id
        print(f"POST URL: {url}")
        with self.session as session:
            response = session.get(url)
        return response