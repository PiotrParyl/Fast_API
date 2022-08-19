
from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None




my_data = {
    1:{
        "name":"Kula",
        "price":25,
        "brand":"psk",
    },

    2:{
        "name":"Nowak",
        "price":45,
        "brand":"paruszowiec",
    }
}




@app.get("/")
def home():
    return {"Data":"kiila"}

@app.get("/test1")
def test1():
    return {"data1":"data1"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="siema elo test")):
    return my_data[item_id]

@app.get("/get-by-name/")
def get_item(name: str):
    for item in my_data:
        if my_data[item]['name']== name:
            return my_data[item]
    return {"Data":"Not founddd"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in my_data:
        return {"Error":"Item ID alredy exists"}

    my_data[item_id] = item

    return my_data[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in my_data:
        return {"Error":"Idem ID does'n exist"}
    my_data[item_id].update(item)
    return my_data[item_id]


@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="the id of the item to delete ")):
    if item_id not in my_data:
        return {"Error":"ID does not exist"}
    del my_data[item_id]
    return {"Success": "Item deleted!"}
    