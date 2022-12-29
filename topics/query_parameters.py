from .router import router
from typing import Optional
from fastapi_utils.cbv import cbv


@cbv(router)
class QueryParameters:
    @router.get("/query_components/")  # query parameter
    async def get_query_components(self, number: Optional[int], text: str = "sahil"):
        return {"number": number, "text": text}
