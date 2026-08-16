# 🍽️ MenuFlow

> Transform any restaurant menu photo into a structured, searchable, editable digital menu using OCR, AI, and FastAPI.

---

## 🚀 Overview

MenuFlow is an AI-powered web application that automates one of the most repetitive tasks in the restaurant industry: converting printed menus into digital menus.

Instead of manually entering dozens of products, categories, and prices, a restaurant owner can simply upload a photo of a menu.

MenuFlow will:

1. Extract text from the image using OCR
2. Understand and structure the menu using AI
3. Organize products into categories
4. Store everything in a database
5. Generate a clean web menu
6. Provide a full admin panel for management
7. Export the menu as a PDF

The result is a complete digital menu created automatically from a single image.

---

# ✨ Features

## 📸 Menu Image Upload

Upload a menu photo from any restaurant.

Supported examples:

* Printed menus
* Restaurant flyers
* Scanned menus
* Phone photos

---

## 🔍 OCR Text Extraction

MenuFlow extracts raw text from the uploaded image.

Example:

Before:

```text
PIZZA

Pizza Margherita 35 lei
Pizza Diavola 40 lei

PASTA

Carbonara 36 lei
```

After OCR:

```text
Pizza Margherita 35 lei
Pizza Diavola 40 lei
Carbonara 36 lei
```

---

## 🤖 AI Menu Understanding

Raw OCR text is processed by AI.

The model identifies:

* Categories
* Product names
* Prices

Example:

```json
[
  {
    "category": "Pizza",
    "name": "Pizza Margherita",
    "price": "35 lei"
  },
  {
    "category": "Pizza",
    "name": "Pizza Diavola",
    "price": "40 lei"
  }
]
```

---

## 💾 Database Storage

All extracted products are stored in SQLite using SQLAlchemy.

Each item contains:

```text
ID
Category
Product Name
Price
```

---

## 🍽️ Dynamic Menu Generation

MenuFlow automatically creates a structured menu page.

Example:

```text
Pizza
 ├─ Pizza Margherita ........ 35 lei
 ├─ Pizza Diavola ........... 40 lei

Pasta
 ├─ Carbonara ............... 36 lei
```

---

## 🔎 Search Functionality

Users can instantly search for products.

Examples:

```text
pizza
carbonara
espresso
cola
```

Results are filtered in real time.

---

## ⚙️ Admin Panel

The application includes a complete management interface.

### Features

* ➕ Add Products
* ✏️ Edit Products
* 🗑 Delete Products
* 🔎 Search Products
* 📄 Export PDF

No database knowledge is required.

---

## ✏️ Edit Products

Restaurant owners can modify:

* Category
* Product Name
* Price

directly from the browser.

---

## ➕ Add Products

New products can be inserted manually through the Admin Panel.

Example:

```text
Category: Dessert
Name: Tiramisu
Price: 22 lei
```

---

## 🗑 Delete Products

Products can be safely removed.

A confirmation dialog prevents accidental deletion.

---

## 🔄 Automatic Menu Replacement

When a new menu image is uploaded:

```text
Old Menu
     ↓
Removed
     ↓
New Menu
```

The application always displays the latest uploaded menu.

This prevents multiple restaurant menus from being mixed together.

---

## 📄 PDF Export

Generate a downloadable PDF version of the menu with one click.

Perfect for:

* Printing
* Sharing
* Archiving
* Client delivery

---

# 🏗 Architecture

```text
Menu Image
     │
     ▼
OCR Extraction
     │
     ▼
AI Processing
     │
     ▼
Structured Menu Data
     │
     ▼
SQLite Database
     │
     ├────────► Admin Panel
     │
     ├────────► Web Menu
     │
     └────────► PDF Export
```

---

# 🛠 Tech Stack

### Backend

* Python
* FastAPI

### Database

* SQLite
* SQLAlchemy

### AI

* OpenRouter API
* Large Language Models

### OCR

* OCR Engine Integration

### Frontend

* HTML
* CSS
* Jinja2 Templates

### Utilities

* ReportLab (PDF Generation)

---

# 📂 Project Structure

```text
MenuFlow
│
├── main.py
├── ai.py
├── ocr.py
├── database.py
├── models.py
├── menuflow.db
│
├── templates
│   ├── admin.html
│   ├── menu.html
│   ├── add.html
│   └── edit.html
│
├── static
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/biancarebeca/MenuFlow.git
```

Move into the project:

```bash
cd MenuFlow
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the server:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

# 📍 Available Routes

| Route          | Description           |
| -------------- | --------------------- |
| `/`            | Home                  |
| `/upload`      | Upload Menu Image     |
| `/view-menu`   | View Generated Menu   |
| `/admin`       | Admin Panel           |
| `/add`         | Add Product           |
| `/edit/{id}`   | Edit Product          |
| `/delete/{id}` | Delete Product        |
| `/all-items`   | JSON Data             |
| `/export-pdf`  | Export Menu PDF       |
| `/docs`        | FastAPI Documentation |

---

# 🎯 Key Challenges Solved

### OCR Noise

Restaurant menus are often inconsistent, blurry, or poorly formatted.

MenuFlow extracts usable text and prepares it for AI processing.

### Menu Structure Detection

The application converts unstructured text into structured data.

### Digitalization Automation

What normally requires manual data entry is reduced to a single image upload.

### Content Management

The Admin Panel allows complete control over generated content.

---

# 📈 Future Improvements

* Multi-language menu support
* Cloud database support
* User authentication
* Multiple restaurant management
* Public shareable menu links
* Image gallery for products
* QR Code generation
* Analytics dashboard

---

# 👩‍💻 Author

**Bianca Rebeca**

MenuFlow was built as a portfolio project to demonstrate practical experience with:

* FastAPI
* OCR Processing
* AI Integration
* SQLAlchemy
* Database Design
* CRUD Operations
* PDF Generation
* Full-Stack Application Development

---

# ⭐ Why This Project Matters

MenuFlow combines multiple modern technologies into a real-world business solution.

Instead of being a simple CRUD application, it demonstrates the complete pipeline of:

```text
Image Processing
        +
Artificial Intelligence
        +
Backend Development
        +
Database Management
        +
User Interface Design
        +
Document Generation
```

all inside a single production-style application.

