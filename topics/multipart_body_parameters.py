from pydantic import BaseModel
from typing import Optional
from fastapi_utils.cbv import cbv
from .router import router
from fastapi import Form


@cbv(router)
class MultipartBodyParameters:
    @router.post("/employee-form/")  # body parameter
    def make_package(self, name: str = Form(...), type=Form(...)):
        return {"name": name, "type": type}
