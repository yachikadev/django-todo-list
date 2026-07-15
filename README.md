# ✅ Django Todo List App

A simple and clean todo list web application built with Django. You can add tasks, mark them as complete, and delete them — all in one place.

> Built by [Yachika Sharma](https://github.com/yachikadev) 

---

## 🚀 Features

- Add new tasks
- Mark tasks as complete / incomplete
- Delete tasks
- Clean and minimal UI
- Django Admin panel support

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3.x | Backend language |
| Django | Web framework |
| SQLite | Default database |
| HTML & CSS | Frontend templates |

---


## ⚙️ Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/yachikadev/django-todo-list.git
cd django-todo-list

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. (Optional) Create superuser for admin panel
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Open in browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📁 Project Structure

```
django_todo/
├── manage.py
├── requirements.txt
├── todoproject/         # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── todos/               # Todo app
    ├── models.py        # Todo model
    ├── views.py         # List, add, toggle, delete views
    ├── forms.py         # TodoForm
    ├── urls.py          # App URLs
    ├── admin.py         # Admin registration
    └── templates/todos/
        ├── base.html
        └── todo_list.html
```

---

## 👩‍💻 About Me

Hi! I'm **Yachika Sharma**, a developer who loves building clean and useful web apps.  
Feel free to explore my work: [github.com/yachikadev](https://github.com/yachikadev)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
