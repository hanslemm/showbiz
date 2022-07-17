from faker import Faker
from dataclasses import dataclass
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Boolean, Float

@dataclass
class Showbiz:
    name: str = None
    description: str = None
    db: str = None
    db_user: str = None
    db_password: str = None
    engine: create_engine = None
    meta: MetaData = None

    def __post_init__(self):
        if self.db is not None:
            self.engine = create_engine(f'sqlite:///{self.db}')
            self.meta = MetaData()
            self.meta.create_all(self.engine)
            self.init_db()
        self.engine = create_engine(f'postgresql://{self.db_user}:{self.db_password}@{self.db}')
