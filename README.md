# Django PostgreSQL Project

## Project Overview

# Description
This project is a web-based application designed to facilitate the rental of unmanned aerial vehicles (UAVs), commonly referred to as drones. The platform caters to both individual enthusiasts and professional users by offering a user-friendly interface to browse, book, and manage drone rentals. The key objective is to streamline the process of renting drones, ensuring a seamless transaction from booking to flying, thereby addressing the growing demand for accessible UAV technology for various applications such as aerial photography, surveillance, and recreational flying.

# Unique Problem Solved
The unique problem addressed by this project lies in providing a centralized platform where users can access a variety of drones tailored to their specific needs without the hassle of contacting multiple vendors or dealing with complex logistics. By integrating features such as instant bookings, comprehensive drone specifications, and user account management, the platform removes significant barriers typically encountered in the drone rental market. Additionally, it enhances user engagement through a robust, secure, and scalable system.

# Core Features
User Authentication System
Allows users to sign up, log in, and manage their profiles.
Ensures that drone rental activities are securely associated with authenticated users.

Drone Management
Admins can add, delete, update, and list drones available for rent.
Each drone listing includes details such as brand, model, weight, and category.
Rental Management

Users can view available drones and book them based on specific dates and times.
Users can manage their rentals by listing active and past rentals, updating booking times, or cancelling bookings.

Advanced Search and Filtering
Provides the ability to filter and search through the list of drones and rentals, enhancing user experience by allowing quick access to needed resources.

## Features

List the features of your project such as:
- User authentication (login, logout, sign up)
- Drone rental system
- Admin panel for managing drones

## Technology Stack

- **Backend Framework:** Django 3.1
- **Database:** PostgreSQL
- **Frontend Technologies:** HTML, CSS (Bootstrap), JavaScript (optional jQuery)
- **Other Dependencies:** See `requirements.txt`

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

# Clone the repository
git clone https://github.com/itu-itis21-gursu20/baykar-rent-drone-project.git

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Set up your PostgreSQL database
It is explained how to configure the database settings in settings.py

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver

The program starts at http://127.0.0.1:8000/ in your web browser
If you want to enter administration system of program, you should enter http://127.0.0.1:8000/admin/ url.

# Running Tests
python manage.py test


