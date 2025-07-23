# Company–Employee RESTful API

A RESTful API built using **Django** and **Django REST Framework (DRF)** to manage companies and their associated employees.

## 🔧 Features

- CRUD operations for Companies and Employees
- Custom endpoint: `/companies/{id}/employees/` to get employees by company
- Filter employees by category
- Nested serializers to include related company data in employee API
- JSON-only API responses (Browsable API disabled for production)
- Permissions: Read-only access for unauthenticated users
- Tested using Django Browsable API and Postman

## 🏗 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default)
- Postman (for testing)

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
