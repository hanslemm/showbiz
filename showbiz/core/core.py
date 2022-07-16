from faker import Faker
from dataclasses import dataclass

@dataclass
class ShowBiz:
    name: str
    description: str

    def db_config(self, driver, ):
