from fastapi import FastAPI, UploadFile, File, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from collections import defaultdict

from ocr import extract_text
from ai import organize_menu

from database import engine, SessionLocal
from models import Base, MenuItem

app = FastAPI()

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

menu_data = []


@app.get("/")
def home():
    return {"message": "Salut, MenuFlow merge!"}


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    global menu_data

    content = await file.read()

    with open("temp_image.jpg", "wb") as f:
        f.write(content)

    result = extract_text("temp_image.jpg")

    text = "\n".join(result)

    menu = organize_menu(text)

    db = SessionLocal()

    for item in menu:

        db_item = MenuItem(
            category=item["category"],
            name=item["name"],
            price=item["price"]
        )

        db.add(db_item)

    db.commit()
    db.close()

    menu_data = menu

    return {
        "menu": menu
    }


@app.get("/view-menu")
def view_menu(request: Request):

    db = SessionLocal()

    items = db.query(MenuItem).all()

    db.close()

    grouped_menu = defaultdict(list)

    for item in items:

        grouped_menu[item.category].append(
            {
                "name": item.name,
                "price": item.price
            }
        )

    return templates.TemplateResponse(
        request,
        "menu.html",
        {
            "menu": grouped_menu
        }
    )


@app.get("/all-items")
def all_items():

    db = SessionLocal()

    items = db.query(MenuItem).all()

    db.close()

    return [
        {
            "id": item.id,
            "category": item.category,
            "name": item.name,
            "price": item.price
        }
        for item in items
    ]