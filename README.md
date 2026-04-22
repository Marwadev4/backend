# Font & Theme Management API

A professional Flask backend API for managing font uploads, theme collections, and downloadable theme packages.

## Features

- **Font Management**: Upload, list, view, update, and delete font files
- **Secure File Handling**: Magic byte validation, file extension whitelist, path traversal prevention
- **Download Packages**: Generate ZIP archives containing theme metadata and font files
- **Clean Architecture**: Separation of concerns with services, models, schemas, and API layers

## Project Structure

```
font_theme_api/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── config.py              # Configuration settings
│   ├── extensions.py          # Flask extensions initialization
│   ├── api/                   # API endpoints
│   │   ├── fonts.py           # Font management endpoints
│   ├── models/                # Database models
│   │   ├── font.py            # Font model
│   ├── services/              # Business logic layer
│   │   ├── font_service.py    # Font operations
│   │   └── file_service.py    # File handling with security
│   ├── schemas/               # Serialization schemas
│   ├── utils/                 # Utility functions
│   └── errors/                # Error handlers
├── uploads/                   # Font file storage
├── tests/                     # Unit tests
├── requirements.txt          # Python dependencies
└── run.py                     # Application entry point
```

## Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

## Configuration

Configure the application using environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | `development` | Environment: development, production, testing |
| `FLASK_HOST` | `0.0.0.0` | Host to bind to |
| `FLASK_PORT` | `5000` | Port to bind to |
| `SECRET_KEY` | `dev-secret-key` | Application secret key |
| `DATABASE_URL` | SQLite file | Database connection string |
| `FORCE_HTTPS` | `false` | Enforce HTTPS (production) |

## API Endpoints

### Font Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/fonts/upload` | Upload a font file |
| GET | `/api/fonts` | List all fonts |
| GET | `/api/fonts/<id>` | Get font details |
| PUT | `/api/fonts/<id>` | Update font metadata |
| DELETE | `/api/fonts/<id>` | Delete a font |
| GET | `/api/fonts/<id>/download` | Download font file |

## Usage Examples

### Upload a Font

```bash
curl -X POST http://localhost:5000/api/fonts/upload \
  -F "file=@path/to/font.ttf" \
  -F "name=My Font" \
  -F "family=MyFontFamily" \
  -F "style=regular"
```

### Download Font

```bash
curl -O http://localhost:5000/api/fonts/download/1
```

## Security Features

- **File Validation**: Magic byte verification for font files
- **Extension Whitelist**: Only .ttf, .otf, .woff, .woff2 allowed
- **File Size Limit**: Maximum 10MB per file
- **Path Traversal Prevention**: Secure filename handling
- **CORS Configuration**: Configurable cross-origin requests
- **Input Sanitization**: All user inputs validated and sanitized

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_fonts.py
```

## Environment Support

- **Development**: Debug mode enabled, local SQLite database
- **Production**: Optimized settings, HTTPS enforcement available
- **Testing**: In-memory database, test client provided
