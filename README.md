# 🍽️ MenuFlow

> Transform a restaurant menu photo into a structured, editable digital menu using OCR, AI, and FastAPI.

---

## 🚀 Overview

MenuFlow automates the process of converting printed restaurant menus into digital menus.

Upload a menu image and the application will:

* Extract text using OCR
* Organize products with AI
* Save menu items to a database
* Generate a web menu automatically
* Provide a full admin panel
* Export the menu as a PDF

---

## ✨ Features

### 📸 Menu Upload

Upload a photo of a restaurant menu.

### 🔍 OCR Processing

Extracts text from the image automatically.

### 🤖 AI Menu Structuring

Identifies:

* Categories
* Product names
* Prices

and converts them into structured data.

### 💾 Database Storage

Stores menu items using SQLite and SQLAlchemy.

### 🍽️ Dynamic Menu Page

Displays products grouped by category.


### ⚙️ Admin Panel

Manage menu items directly from the browser.

Features include:

* ➕ Add Product
* ✏️ Edit Product
* 🗑 Delete Product
* 🔎 Search Products

### 📄 PDF Export

Generate and download a PDF version of the current menu.

### 🔄 Menu Replacement

Uploading a new menu automatically replaces the previous one.

---

## 🏗 Workflow

```text
Menu Image
     ↓
OCR Extraction
     ↓
AI Processing
     ↓
Structured Menu
     ↓
SQLite Database
     ↓
Web Menu + Admin Panel
     ↓
PDF Export
```

---

## 🛠 Tech Stack

### Backend

* Python
* FastAPI

### Database

* SQLite
* SQLAlchemy

### AI & OCR

* OpenRouter API
* OCR Processing

### Frontend

* HTML
* CSS
* Jinja2

### Utilities

* ReportLab (PDF Generation)

---

## 📂 Project Structure

```text
MenuFlow/
│
├── main.py
├── ai.py
├── ocr.py
├── database.py
├── models.py
│
├── templates/
│   ├── menu.html
│   ├── admin.html
│   ├── add.html
│   └── edit.html
│
├── static/
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/biancarebeca/MenuFlow.git
cd MenuFlow
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 📍 Available Routes

| Route          | Description           |
| -------------- | --------------------- |
| `/view-menu`   | Display menu          |
| `/admin`       | Admin panel           |
| `/add`         | Add product           |
| `/edit/{id}`   | Edit product          |
| `/delete/{id}` | Delete product        |
| `/all-items`   | JSON data             |
| `/export-pdf`  | Export PDF            |
| `/docs`        | FastAPI documentation |

---

## 🎯 What This Project Demonstrates

* OCR Integration
* AI-Powered Data Extraction
* FastAPI Development
* SQLAlchemy & SQLite
* CRUD Operations
* PDF Generation
* Full-Stack Web Application Development

---

## 👩‍💻 Author

**Bianca Rebeca**

Built as a portfolio project showcasing how OCR and AI can automate the creation and management of restaurant menus.
