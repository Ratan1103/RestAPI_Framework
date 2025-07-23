# 🚀 Django REST API Framework

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/Django_REST-Framework-ff1709?style=for-the-badge&logo=django&logoColor=white)](https://django-rest-framework.org)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)](https://github.com/your-username/RestAPI_Framework/graphs/commit-activity)

</div>

<p align="center">
  <strong>A fully functional RESTful API built with Django & Django REST Framework</strong><br>
  Supporting student, course, and department management with clean modular architecture
</p>

---

## ✨ Features

<table>
<tr>
<td>

### 🏗️ **Architecture**
- ✅ Django 4.x + Django REST Framework
- ✅ Modular structure & clean code
- ✅ SQLite database integration
- ✅ Custom pagination & filtering
- ✅ RESTful API design principles

</td>
<td>

### 🔧 **Functionality**
- ✅ Complete CRUD operations
- ✅ Students management
- ✅ Courses management  
- ✅ Departments management
- ✅ Basic HTML UI for testing

</td>
</tr>
</table>

## 🏛️ Project Architecture

```
RestAPI_Framework-main/
┣ 📂 api/                    # 🧠 Business logic: views, filters, pagination
┣ 📂 students/               # 👥 Models, serializers, views for students
┣ 📂 rest_main/              # ⚙️ Project settings and routing
┣ 📂 templates/              # 🎨 Basic HTML page with navigation
┣ 📄 db.sqlite3              # 🗄️ SQLite database
┣ 📄 manage.py               # 🔧 Django management utility
┗ 📄 requirements.txt        # 📦 Project dependencies
```

## 🚀 Quick Start

### Prerequisites

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-Latest-orange?logo=git&logoColor=white)

### Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/your-username/RestAPI_Framework-main.git
cd RestAPI_Framework-main
```

2️⃣ **Create virtual environment**
```bash
# Using venv
python -m venv .venv

# Activate (Linux/Mac)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt

# Or install manually
pip install django djangorestframework
```

4️⃣ **Database setup**
```bash
python manage.py makemigrations
python manage.py migrate
```

5️⃣ **Run the development server**
```bash
python manage.py runserver
```

🎉 **Visit:** [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📡 API Endpoints

<div align="center">
<table>
<thead>
<tr>
<th>Method</th>
<th>Endpoint</th>
<th>Description</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>GET</code></td>
<td><code>/students/</code></td>
<td>Retrieve all students</td>
<td>✅</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/student/&lt;id&gt;/</code></td>
<td>Retrieve student by ID</td>
<td>✅</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/courses/</code></td>
<td>Retrieve all courses</td>
<td>✅</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/course/&lt;id&gt;/</code></td>
<td>Retrieve course by ID</td>
<td>✅</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/departments/</code></td>
<td>Retrieve all departments</td>
<td>✅</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/department/</code></td>
<td>Retrieve department details</td>
<td>✅</td>
</tr>
</tbody>
</table>
</div>

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

Add your test cases in `tests.py` files within the `students/` and `api/` directories.

## 🎨 Frontend Preview

A minimal UI is available via `main.html` in the `templates/` directory. Interactive buttons are provided to test API endpoints directly in your browser.

## 🛠️ Development

### Tech Stack

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
<img src="https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white" alt="Django REST Framework">
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
</p>

### Code Quality

- **Modular Architecture**: Clean separation of concerns
- **RESTful Design**: Following REST API best practices
- **Extensible**: Easy to add new features and modules
- **Maintainable**: Well-structured codebase

## 🤝 Contributing

We love contributions! Here's how you can help:

1. 🍴 **Fork** the repository
2. 🌿 **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. 💻 **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. 📤 **Push** to the branch (`git push origin feature/amazing-feature`)
5. 🔀 **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

## 📞 Support

<div align="center">

[![GitHub Issues](https://img.shields.io/badge/GitHub-Issues-red?style=for-the-badge&logo=github)](https://github.com/Ratan1103/RestAPI_Framework/)
[![Email](https://img.shields.io/badge/Email-Contact-blue?style=for-the-badge&logo=gmail)](mailto:sanjayratan665@gmail.com)

</div>

If you have any questions, feel free to:
- 🐛 [Open an issue](https://github.com/Ratan1103/RestAPI_Framework/issues)
- 📧 Send an email to `sanjayratan665@gmail.com`
- 💬 Start a discussion in the repository

---

<div align="center">
<p>Made with ❤️ by <a href="https://github.com/Ratan1103">Ratan Sanjay</a></p>
<p>⭐ Star this repo if you found it helpful!</p>
</div>
