from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
    return {"Hello": "World"}


@app.get("/components/{component_id}")
async def get_component(component_id):
    return {"component_id": component_id}


@app.get("/specific_components/{component_id}")
async def get_specific_component(component_id: int):
    return {"specific_component_id": component_id}
