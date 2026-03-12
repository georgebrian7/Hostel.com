# Hostels - Django Booking & Property Management Platform

A Django-based web application for booking hostels and managing hostel properties. This project consists of a public booking platform and a private dashboard for hostel owners to list and manage their properties.

## 🎯 Features

### Guest Features
- **Browse Hostels** - Search and filter available hostels by location, price, and amenities
- **Detailed Listings** - View comprehensive hostel information with photos, ratings, and reviews
- **Easy Booking** - Seamless reservation system with instant confirmation
- **Manage Bookings** - Track and manage your reservations from your account
- **Reviews & Ratings** - Leave feedback and read reviews from other guests
- **User Dashboard** - Centralized hub for bookings, saved properties, and profile management

### Host/Owner Features
- **Property Dashboard** - Complete management suite for hostel properties
- **Post Properties** - Create detailed hostel listings with images, amenities, and pricing
- **Manage Bookings** - View and process guest reservations
- **Property Analytics** - Track bookings, occupancy rates, and revenue
- **Edit Listings** - Update property information, availability, and pricing
- **Guest Management** - Track guests and manage communications

## 🛠️ Tech Stack

- **Backend Framework:** Django 3.2+
- **Database:** MySQL
- **Frontend:** Django Templates + Bootstrap/CSS
- **Authentication:** Django built-in auth system
- **ORM:** Django ORM
- **Environment Management:** python-dotenv

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL Server 5.7 or higher
- pip (Python package manager)
- virtualenv

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/hostels.git
cd hostels
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```env
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_ENGINE=django.db.backends.mysql
DB_NAME=hostels_db
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=3306
```

### 5. Create MySQL Database
```sql
CREATE DATABASE hostels_db;
CREATE USER 'hostel_user'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON hostels_db.* TO 'hostel_user'@'localhost';
FLUSH PRIVILEGES;
```

### 6. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 8. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 9. Run Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.


### Booking System
- Guests select dates and room type
- Real-time availability check



### Search & Filter
- Filter by location, price range, amenities
- Sort by rating, price, new listings
- Advanced search with multiple criteria



**Note:** This is a development version. For production deployment, follow the security guidelines and deployment checklist above. Live payment integration and advanced features are not included in this version.
