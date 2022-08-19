from msilib.schema import Patch
from pathlib import Path
from fastapi import FastAPI


app = FastAPI()

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

@app.get("/get_item/{item_id}")
def get_item(item_id: int = Path()):
    return my_data[item_id]

