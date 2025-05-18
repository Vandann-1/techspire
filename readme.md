# TechSpire Project

A modern web application built with Django and TailwindCSS showcasing company projects and founders.

## Getting Started

### Prerequisites
- Python 3.8+
- Django 5.0+
- Virtual Environment (recommended)

### Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd techspire
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install django
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

```
techspire/
├── Techproject/        # Project configuration
├── techspire/          # Main application
│   ├── templates/      # HTML templates
│   ├── static/        # Static files
│   ├── views.py       # View functions
│   └── models.py      # Data models
└── manage.py          # Django management script
```

## Available Routes

| Route | View Function | Description | Template |
|-------|--------------|-------------|-----------|
| `/` | `home` | Home page with company overview | `home.html` |
| `/projects` | `projectsho` | Projects showcase page | `projects.html` |
| `/founders` | `founders` | Team and founders page | `founder.html` |

## Development

### Adding New Pages
1. Create template in `templates/`
2. Add view function in `views.py`
3. Add URL pattern in `urls.py`

### Static Files
- Place all static files (images, CSS, JS) in `static/` directory
- Reference them in templates using:
```html
{% load static %}
<img src="{% static 'path/to/file' %}">
```

## Production Deployment Notes

1. Set `DEBUG = False` in settings.py
2. Update `ALLOWED_HOSTS`
3. Configure static files serving
4. Set up proper database settings
5. Update `SECRET_KEY`

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## License

MIT License - Feel free to use and modify for your projects.
