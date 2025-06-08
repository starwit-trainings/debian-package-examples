"""Example for library usage - config class"""

from pydantic import BaseModel, Field
from typing_extensions import Annotated

class ApplicationConfig(BaseModel):
    host: str = 'localhost'
    port: Annotated[int, Field(ge=1, le=65536)] = 6379
    some_field: str = 'sample_value'