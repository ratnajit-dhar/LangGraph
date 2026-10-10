# to create a graph, we need to first create a state

import os
from typing import TypedDict
# 1) Typed Dictionary

class State(TypedDict):
    topic : str
    summary : str
    score : str

# 2) Pydantic approach(Good for data validation)

from pydantic import BaseModel, field_validator

class State(BaseModel):
    topic : str
    summary : str 
    score : str = ""

    @field_validator
    def score_positive(cls, v):
        if v<0:
            raise ValueError("Score must be positive")


# 3) Python Data Classes(Used rarely)

from dataclasses import dataclass, field

@dataclass
class State:
    topic : str = ""
    summary : str = ""
    messages : list = field(default_factory = list)


# 4) Using Langgraph

from langgraph.graph import MessageState

class State(MessageState):
    user_name: str
    language: str
