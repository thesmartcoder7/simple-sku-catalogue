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

 Clone the repository:

```bash
git clone https://github.com/thesmartcoder7/simple-sku-catalogue.git
cd simple-sku-catalogue
   ```

## Development

To run the application in development mode:

1. Start the backend:

    You can use specific commands within just to do your basic mundane stuff in the django backend. They are all in the backend folder's Makefile. But some of the common ones include . . .

   ```bash
   cd sku-backend

    python manage.py runserver 0.0.0.0:8000

    python manage.py makemigrations && python manage.py migrate

    python manage.py createsuperuser

    python manage.py test
   ```

2. Start the frontend:

   ```bash
   cd sku-frontend

   npm install

   npm build

   npm run dev
   ```

Access the application:

- Frontend: <http://localhost:3000>
- Backend API: <http://localhost:8000/api/skus/>

## API Endpoints

- `GET /api/skus/`: List all medication SKUs
- `POST /api/skus/`: Create a new medication SKU
- `GET /api/skus/<id>/`: Retrieve a specific medication SKU
- `PUT /api/skus/<id>/`: Update a specific medication SKU
- `DELETE /api/skus/<id>/`: Delete a specific medication SKU

## Testing

To run the backend tests:

```bash
cd sku-backend

python manage.py test
```

## Deployment

The application can containerized and  easily deployed to any Docker-compatible hosting service. Make sure to update the `ALLOWED_HOSTS` in the Django settings before deployment . . . ow and any other configurations as well.

## Sample Data

Database Population: If you want to populate your database directly, you can create a Django management command or use the Django shell to insert this data. or the Frontend but in case you want starter data, you can use the shell and load this simple set.

```bash
python manage.py shell
```

```bash
from sku_catalogue.models import MedicationSKU

sample_data = [
    {
        "medication_name": "Paracetamol",
        "dose": "500mg",
        "presentation": "Tablet",
        "unit": "Box of 30",
        "countries": "Kenya, Nigeria, Ghana"
    },
    {
        "medication_name": "Amoxicillin",
        "dose": "250mg",
        "presentation": "Capsule",
        "unit": "Bottle of 100",
        "countries": "Ethiopia, Tanzania, Uganda"
    },
    {
        "medication_name": "Metformin",
        "dose": "850mg",
        "presentation": "Extended-release tablet",
        "unit": "Box of 60",
        "countries": "South Africa, Egypt, Morocco"
    },
    {
        "medication_name": "Ibuprofen",
        "dose": "400mg",
        "presentation": "Film-coated tablet",
        "unit": "Blister pack of 24",
        "countries": "Senegal, Cameroon, Ivory Coast"
    },
    {
        "medication_name": "Omeprazole",
        "dose": "20mg",
        "presentation": "Enteric-coated capsule",
        "unit": "Box of 28",
        "countries": "Rwanda, Zambia, Mozambique"
    }
]

for item in sample_data:
    MedicationSKU.objects.create(**item)
```

## License

[Licence](LICENCE)
