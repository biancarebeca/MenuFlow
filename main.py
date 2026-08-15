from fastapi import FastAPI, UploadFile, File, Request, Form
from fastapi.responses import RedirectResponse
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


@app.get("/")
def home():
    return {"message": "Salut, MenuFlow merge!"}


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    content = await file.read()

    with open("temp_image.jpg", "wb") as f:
        f.write(content)

    result = extract_text("temp_image.jpg")

    text = "\n".join(result)

    menu = organize_menu(text)

    db = SessionLocal()

    # Sterge meniul vechi
    db.query(MenuItem).delete()
    db.commit()

    for item in menu:

        existing = db.query(MenuItem).filter(
            MenuItem.name == item["name"],
            MenuItem.price == item["price"]
        ).first()

        if existing:
            continue

        db_item = MenuItem(
            category=item["category"],
            name=item["name"],
            price=item["price"]
        )

        db.add(db_item)

    db.commit()
    db.close()

    return {
        "menu": menu
    }


@app.get("/view-menu")
def view_menu(
    request: Request,
    search: str = ""
):

    db = SessionLocal()

    if search:

        items = db.query(MenuItem).filter(
            MenuItem.name.contains(search)
        ).all()

    else:

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
            "menu": grouped_menu,
            "search": search
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


@app.get("/admin")
def admin(request: Request):

    db = SessionLocal()

    items = db.query(MenuItem).all()

    db.close()

    return templates.TemplateResponse(
        request,
        "admin.html",
        {
            "items": items
        }
    )


@app.get("/delete/{item_id}")
def delete_item(item_id: int):

    db = SessionLocal()

    item = db.query(MenuItem).filter(
        MenuItem.id == item_id
    ).first()

    if item:
        db.delete(item)
        db.commit()

    db.close()

    return RedirectResponse(
        url="/admin",
        status_code=303
    )


@app.get("/edit/{item_id}")
def edit_page(request: Request, item_id: int):

    db = SessionLocal()

    item = db.query(MenuItem).filter(
        MenuItem.id == item_id
    ).first()

    db.close()

    return templates.TemplateResponse(
        request,
        "edit.html",
        {
            "item": item
        }
    )


@app.post("/edit/{item_id}")
def save_edit(
    item_id: int,
    category: str = Form(...),
    name: str = Form(...),
    price: str = Form(...)
):

    db = SessionLocal()

    item = db.query(MenuItem).filter(
        MenuItem.id == item_id
    ).first()

    if item:

        item.category = category
        item.name = name
        item.price = price

        db.commit()

    db.close()

    return RedirectResponse(
        url="/admin",
        status_code=303
    )


@app.get("/add")
def add_page(request: Request):

    return templates.TemplateResponse(
        request,
        "add.html",
        {}
    )


@app.post("/add")
def save_new_product(
    category: str = Form(...),
    name: str = Form(...),
    price: str = Form(...)
):

    db = SessionLocal()

    item = MenuItem(
        category=category,
        name=name,
        price=price
    )

    db.add(item)

    db.commit()

    db.close()

    return RedirectResponse(
        url="/admin",
        status_code=303
    )

@app.get("/fix-categories")
def fix_categories():

    db = SessionLocal()

    items = db.query(MenuItem).all()

    for item in items:

        if item.category in [
            "Drink",
            "Drinks",
            "Beverages",
            "Beverage"
        ]:
            item.category = "Bauturi"

        elif item.category in [
            "Salads",
            "Salad"
        ]:
            item.category = "Salate"

        elif item.category in [
            "Pasta"
        ]:
            item.category = "Paste"

    db.commit()
    db.close()

    return {
        "status": "ok"
    }