# Medication SKU Catalogue

## Overview

The Medication SKU Catalogue is a web application designed to manage a catalogue of medication Stock Keeping Units (SKUs). It provides a user-friendly interface for creating, reading, updating, and deleting medication SKUs. This project is built with a Django backend API and a Next.js frontend, containerized using Docker for easy deployment and development.

## Features

- Create new medication SKUs
- View a list of all medication SKUs
- Update existing medication SKUs
- Delete medication SKUs
- Responsive web interface
- RESTful API backend
- Containerized application for easy deployment

## Tech Stack

- Backend:
  - Django
  - Django REST Framework
  - SQLite (for development)
- Frontend:
  - Next.js
  - React
  - Material-UI
  - Axios for API calls
- Containerization:
  - Docker
  - Docker Compose

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/thesmartcoder7/simple-sku-catalogue.git
   cd simple-sku-catalogue
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

   or if you are required to run this as root

   ```bash
   sudo docker-compose up --build
   ```

3. Access the application:
   - Frontend: <http://localhost:3000>
   - Backend API: <http://localhost:8000/api/skus/>

## API Endpoints

- `GET /api/skus/`: List all medication SKUs
- `POST /api/skus/`: Create a new medication SKU
- `GET /api/skus/<id>/`: Retrieve a specific medication SKU
- `PUT /api/skus/<id>/`: Update a specific medication SKU
- `DELETE /api/skus/<id>/`: Delete a specific medication SKU

## Development

To run the application in development mode:

1. Start the backend:

   ```bash
   cd sku-backend
   python manage.py runserver
   ```

2. Start the frontend:

   ```bash
   cd sku-frontend
   npm run dev
   ```

## Testing

To run the backend tests:

```bash
cd sku-backend
python manage.py test
```

## Deployment

The application is containerized and can be easily deployed to any Docker-compatible hosting service. Make sure to update the `ALLOWED_HOSTS` in the Django settings and the `API_BASE_URL` in the frontend before deployment.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
