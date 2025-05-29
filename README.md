# 2G Meets AI

A modern web application that combines the power of AI with 2G technology, built with React, TypeScript, and Django.

## 🚀 Features

- Modern React frontend with TypeScript
- Django backend with RESTful API
- Tailwind CSS for styling
- USSD integration
- SQLite database
- Responsive design

## 🛠️ Tech Stack

### Frontend
- React 19
- TypeScript
- Tailwind CSS
- Vite
- PostCSS

### Backend
- Django
- SQLite
- Python

## 📋 Prerequisites

- Node.js (v16 or higher)
- Python 3.x
- pip (Python package manager)
- npm or yarn

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone [your-repository-url]
cd 2gMeetsAI
```

2. Set up the backend:
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the Django server
python manage.py runserver
```

3. Set up the frontend:
```bash
cd frontendv2

# Install dependencies
npm install

# Start the development server
npm run dev
```

4. Open your browser and navigate to `http://localhost:5173`

## 📁 Project Structure

```
2gMeetsAI/
├── frontendv2/          # React frontend application
│   ├── src/            # Source files
│   ├── components/     # React components
│   └── ...
├── ussd_app/           # USSD application logic
├── superiatech/        # Django project settings
├── staticfiles_collected/  # Static files
└── manage.py           # Django management script
```

## 🔧 Development

- Frontend development server runs on `http://localhost:5173`
- Backend API server runs on `http://localhost:8000`

## 📝 License

[Your License]

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

superiorwech@gmail.com
