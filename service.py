from typing import Generator, Any
from requests import Response, Session
from data import GoogleMapConfig, GoogleMapURLBuilder


class GoogleMapService:
    def __init__(self, config: GoogleMapConfig):
        self.config = config
        self.builder = GoogleMapURLBuilder(config)
        self.session = Session()

    def create_location(self) -> Response:
        url = self.builder.get_create_location_url()
        print(f"POST URL: {url}")
        with self.session as session:
            return session.post(url, self.config.location_body)

    def find_location(self, place_id: str) -> Response:
        url = self.builder.get_find_location_url()+place_id
        print(f"POST URL: {url}")
        with self.session as session:
            return session.get(url)

    def create_multiple_locations(
                                self,
                                count_iterations: int
                                ) -> Generator[Response, Any, None]:
        url = self.builder.get_create_location_url()
        with self.session as session:
            for i in range(count_iterations):
                print(f"POST URL: {url}")
                yield session.post(url, self.config.location_body)