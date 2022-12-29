from fastapi_utils.cbv import cbv
from .router import router


@cbv(router)
class PathParameters:
    @router.get("/components/{component_id}")  # path parameter
    def get_component(self, component_id):
        return {"component_id": component_id}

    @router.get("/specific_components/{component_id}")  # path parameter
    def get_specific_component(self, component_id: int):
        return {"specific_component_id": component_id}
