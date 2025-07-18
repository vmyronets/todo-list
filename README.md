# 📝 TODO List Project

A simple and functional Django-based TODO list application that helps users manage tasks efficiently with support for tagging and status tracking.

## 🚀 Features

- ✅ **Create, edit, and delete tasks**
- 🏷️ **Add tags to tasks** for better organization and categorization
- ✔️ **Mark tasks as complete or incomplete**
- 🔍 **Filter tasks by tags** to find related tasks quickly

## 🛠️ Tech Stack

- **Python 3.x**
- **Backend:** Django
- **Database:** SQLite (default, can be changed)
- **Frontend:** Django Templates + Bootstrap (optional styling)

## 🧪 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/vmyronets/todo-list.git
   cd todo-list
   ````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Open the app**
   Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## 👤 Admin Access

A superuser has already been created for reviewing the project structure:

* **Username:** `admin`
* **Password:** `1qazcde3`

You can log in at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📌 Notes

* This project is built as a practice tool and can be extended with user authentication, task priorities, and REST API support.
* Contributions and improvements are welcome!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
