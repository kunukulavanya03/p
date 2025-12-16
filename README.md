# p

Backend API for p

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign.git))

## Project Structure

```
p/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User authentication and authorization
- CRUD operations for users
- Password reset
- User role management

## API Endpoints

- `POST /api/register` - Create a new user account.
- `POST /api/login` - Log in to the application.
- `GET /api/users` - Get all users.
- `GET /api/users/{user_id}` - Get a user by ID.
- `PUT /api/users/{user_id}` - Update a user.
- `DELETE /api/users/{user_id}` - Delete a user.
- `POST /api/password_reset` - Reset a user's password.

## License

MIT
