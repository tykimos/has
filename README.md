# HAS (Hello Azure Service)

A full-stack web application with FastAPI backend and React frontend.

## Project Structure

```
has/
├── backend/          # FastAPI backend
├── frontend/         # React TypeScript frontend
└── openapi.yaml      # API specification
```

## Getting Started

### Prerequisites

- Python 3.13+
- Node.js 18+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:
   ```bash
   python main.py
   ```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The frontend will be available at `http://localhost:3000`

### Production Build

To build the frontend for production:

```bash
cd frontend
npm run build
```

The build files will be created in `frontend/build/` directory.

## Development

- Backend API documentation is available at `http://localhost:8000/docs` when running the FastAPI server
- The OpenAPI specification is available in `openapi.yaml`

## Deployment

The application is configured for deployment to Azure App Service. The GitHub Actions workflow automatically:

1. Builds the React frontend
2. Copies the build files to `backend/static/`
3. Deploys the FastAPI backend with the static frontend files
