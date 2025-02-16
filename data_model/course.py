from pydantic import Field
from typing import List, Optional

from .node import Node
from .module import Module

class Course(Node):
    """A course structure"""
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)

    modules: List[Module] = Field(default_factory=list)