from pydantic import BaseModel
from typing import Optional
from fastapi_utils.cbv import cbv
from .router import router


class Employee(BaseModel):
    name: str
    age: int
    salary: float
    remarks: Optional[str]


employees = []


@cbv(router)
class BodyParameters:
    @router.get("/employee/")
    async def get_package(self):
        return {"employees": employees}

    @router.post("/employee/")  # body parameter
    def make_package(self, employee: Employee):
        employees.append(employee)
        return {"employee": employee}
