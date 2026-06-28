from pydantic import BaseModel, computed_field


class UserInput(BaseModel):
    sentence:str
    temp:int
    total_words:int

    @computed_field
    @property
    def Temp(self) -> float:
        if self.temp <= 200:
            return self.temp/100