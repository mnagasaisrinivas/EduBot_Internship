# Smart Tutor

Smart Tutor is an AI-powered learning platform that helps students understand complex concepts through interactive explanations, practice problems, quizzes, and study notes. The platform leverages advanced AI to provide personalized tutoring experiences across various subjects.

## 🚀 Features

- **AI-Powered Explanations**: Get step-by-step explanations for questions across different subjects
- **Interactive Q&A**: Ask questions and receive structured answers with detailed steps
- **Practice Problems**: Generate practice problems with solutions for better understanding
- **Quizzes**: Take subject-specific quizzes to test your knowledge
- **Study Notes**: Generate and save comprehensive study notes for topics
- **User Authentication**: Secure login and registration system
- **Content Saving**: Save questions, notes, and quizzes for later reference
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask (Python)
- **Database**: SQLite (with SQLAlchemy ORM)
- **Authentication**: Flask-JWT-Extended
- **Migrations**: Flask-Migrate (Alembic)
- **AI Integration**: LangChain with OpenRouter API
- **CORS Handling**: Flask-CORS

### Frontend
- **Framework**: React (TypeScript)
- **Styling**: Tailwind CSS with shadcn/ui components
- **State Management**: React Query
- **Routing**: React Router DOM
- **Build Tool**: Vite
- **Icons**: Lucide React

## 📋 Project Structure

```
SmartTutor/
├── backend/
│   ├── app/
│   │   ├── __init__.py           # Flask app factory
│   │   ├── config.py             # Configuration settings
│   │   ├── extensions.py         # Flask extensions
│   │   ├── models/               # Database models (User, Note, Question)
│   │   ├── routes/               # API routes (auth, ask, notes, practice, quiz)
│   │   └── utils/                # Utility functions (API calls, AI processing)
│   ├── requirements.txt          # Python dependencies
│   ├── run.py                    # Application entry point
│   └── .env                      # Environment variables
├── frontend/
│   ├── src/
│   │   ├── App.tsx              # Main application component
│   │   ├── main.tsx             # Application entry point
│   │   ├── components/          # Reusable UI components
│   │   ├── contexts/            # React contexts (AuthContext)
│   │   ├── hooks/               # Custom React hooks
│   │   ├── pages/               # Page components (Dashboard, AskQuestion, etc.)
│   │   └── services/            # API service functions
│   ├── package.json             # Node.js dependencies
│   ├── vite.config.ts           # Vite configuration
│   └── .env                     # Environment variables
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+ and npm
- OpenRouter API Key (for AI functionality)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SmartTutor
   ```

2. **Set up the backend**
   ```bash
   # Navigate to the backend directory
   cd backend
   
   # Create a virtual environment
   python -m venv venv
   
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Set up the frontend**
   ```bash
   # Navigate to the frontend directory
   cd ../frontend
   
   # Install dependencies
   npm install
   ```

4. **Configure environment variables**

   Create a `.env` file in the backend directory:
   ```env
   DATABASE_URL=sqlite:///smarttutor.db
   JWT_SECRET_KEY=your-super-secret-jwt-key
   OPENROUTER_API_KEY=your-openrouter-api-key
   ```

### Running the Application

1. **Run the backend server**
   ```bash
   # From the backend directory
   python run.py
   ```
   The backend will start on `http://localhost:5000`

2. **Run the frontend server**
   ```bash
   # From the frontend directory
   npm run dev
   ```
   The frontend will start on `http://localhost:8080`

3. **Access the application**
   Open your browser and go to `http://localhost:8080`

### Building for Production

1. **Build the frontend for production**
   ```bash
   # From the frontend directory
   npm run build
   ```
   This will generate static files in the `output` directory, which will be served by Flask.

## 🧩 API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user
- `GET /api/auth/profile` - Get user profile (requires authentication)

### Questions & Explanations
- `POST /api/ask/` - Get AI explanation for a question (requires authentication)
- `POST /api/ask/save` - Save a question with explanation (requires authentication)
- `GET /api/ask/saved` - Get saved questions for current user (requires authentication)
- `DELETE /api/ask/<question_id>` - Delete a saved question (requires authentication)

### Practice Problems
- `POST /api/practice/` - Generate practice problems (requires authentication)

### Study Notes
- `POST /api/notes/` - Generate study notes (requires authentication)
- `POST /api/notes/save` - Save study notes (requires authentication)
- `GET /api/notes/saved` - Get saved notes for current user (requires authentication)
- `DELETE /api/notes/<note_id>` - Delete a saved note (requires authentication)

### Quizzes
- `POST /api/quiz/generate` - Generate a quiz (requires authentication)

## 🤖 AI Integration

Smart Tutor uses OpenRouter API with LangChain for AI functionality. The AI features include:
- Generating step-by-step explanations for questions
- Creating practice problems with solutions
- Generating comprehensive study notes
- Creating quiz questions with multiple-choice options

To use the AI features, you need to:
1. Get an API key from OpenRouter
2. Set the `OPENROUTER_API_KEY` environment variable

## 📊 Database Models

### User
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email
- `password_hash`: Hashed password
- `created_at`: Account creation timestamp

### Question
- `id`: Primary key
- `user_id`: Foreign key to User
- `subject`: Subject of the question
- `question_text`: The question text
- `answer_steps_list`: JSON list of answer steps
- `answer_summary`: Summary of the answer
- `created_at`: Creation timestamp

### Note
- `id`: Primary key
- `user_id`: Foreign key to User
- `subject`: Subject of the note
- `topic`: Topic of the note
- `heading`: Main heading of the note
- `bullet_points`: JSON list of bullet points
- `created_at`: Creation timestamp

## 🧪 Testing

To run backend tests:
```bash
cd backend
python -m pytest
```

To run frontend tests:
```bash
cd frontend
npm run test
```

## 🔒 Security Features

- JWT-based authentication with secure tokens
- Password hashing using werkzeug.security
- Cross-site request forgery (CSRF) protection
- Input validation and sanitization
- Secure API endpoints with authentication requirements

## 🚀 Deployment

### For Production

1. **Backend Configuration**:
   - Set `JWT_COOKIE_SECURE = True` in production with HTTPS
   - Use a production-ready database (PostgreSQL, MySQL)
   - Add proper error handling and logging

2. **Frontend Configuration**:
   - Build the frontend: `npm run build`
   - The build output will be in the `output` directory
   - Flask will serve the static files from this directory

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions about the project:

1. Check the [Issues](https://github.com/your-username/smart-tutor/issues) page
2. Create a new issue if your problem is not addressed
3. Contact the maintainers via email: [your-email@example.com]

---

## 🚀 About Smart Tutor

Smart Tutor was developed to revolutionize the way students learn by providing personalized, AI-powered tutoring experiences. The platform addresses key challenges in education by offering:

- **Personalized Learning**: Each student receives explanations tailored to their level
- **24/7 Availability**: Access to help anytime, anywhere
- **Interactive Learning**: Engaging content that promotes understanding
- **Progress Tracking**: Save and review previously learned concepts
- **Multi-Subject Support**: Covers various academic subjects

The platform leverages modern web technologies and AI to create an intuitive and effective learning environment that adapts to each student's needs.