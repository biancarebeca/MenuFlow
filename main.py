from fastapi import FastAPI, UploadFile, File, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from collections import defaultdict

from ocr import extract_text
from ai import organize_menu

app = FastAPI()

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

    print("OCR:", result)

    text = "\n".join(result)

    print(text)

    menu = organize_menu(text)

    print(menu)

    menu_data = menu

    return {
        "menu": menu
    }


@app.get("/view-menu")
def view_menu(request: Request):

    grouped_menu = defaultdict(list)

    for item in menu_data:
        grouped_menu[item["category"]].append(item)

    return templates.TemplateResponse(
    request,
    "menu.html",
    {
        "menu": grouped_menu
    }
  )