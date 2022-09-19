from abc import ABC
from datetime import datetime

from car import Car


class SplindlerBattery(Car, ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        num_years = int(self.current_date - self.last_service_date).days / 365.2425
        return num_years > 2