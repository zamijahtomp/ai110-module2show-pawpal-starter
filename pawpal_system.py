from dataclasses import dataclass, field
from typing import List


@dataclass
class Owner:
    name: str
    email: str
    phone: str
    available_minutes: int
    preferences: List[str] = field(default_factory=list)


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    weight_lbs: float
    allergies: List[str] = field(default_factory=list)
    triggers: List[str] = field(default_factory=list)


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    description: str
    preferred_time: str

    def is_feasible(self, available_minutes: int) -> bool:
        pass


class Schedule:
    def __init__(self, date: str, available_minutes: int, owner: Owner, pet: Pet):
        self.date = date
        self.available_minutes = available_minutes
        self.owner = owner
        self.pet = pet
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        pass

    def generate_plan(self) -> List[Task]:
        pass

    def display_plan(self) -> None:
        pass

    def explain_plan(self) -> str:
        pass
