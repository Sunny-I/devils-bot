# AI Chatbot with Google Gemini API

A Django-based AI chatbot application that integrates with Google's Gemini API to provide intelligent conversational responses.

## Features

- Clean and modern web interface
- Real-time chat functionality
- Google Gemini AI integration
- Secure API key management with environment variables
- Responsive design for mobile and desktop
- Typing indicators and smooth animations

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Google Gemini API key

## Setup Instructions

### 1. Clone or Download the Project

```bash
cd ai_chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

1. Open the `.env` file in the project root
2. Replace `your_actual_api_key_here` with your actual Google Gemini API key:

```env
GEMINI_API_KEY=AIzaSyBKA6_aQR6Oq7i631AOAKFB3thswdy6T8g
```

### 4. Get Your Google Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key
5. Paste it in your `.env` file

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

### 7. Access the Application

Open your web browser and navigate to:

```
http://127.0.0.1:8000/
```

## Project Structure

```
ai_chatbot/
├── ai_chatbot/
│   ├── __init__.py
│   ├── settings.py          # Django settings with environment variable loading
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── frontend/
│   ├── __init__.py
│   ├── views.py            # Chat API and home view
│   ├── urls.py             # Frontend URL patterns
│   ├── models.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── templates/
│       └── home_page.html  # Main chat interface
├── .env                    # Environment variables (API keys)
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
└── README.md             # This file
```

## API Endpoints

- `GET /` - Main chat interface
- `POST /api/chat/` - Send message to AI and get response

### Chat API Usage

Send a POST request to `/api/chat/` with JSON payload:

```json
{
  "message": "Your message here"
}
```

Response:

```json
{
  "response": "AI response here",
  "status": "success"
}
```

## Configuration

### Environment Variables

- `GEMINI_API_KEY` - Your Google Gemini API key (required)
- `DJANGO_SECRET_KEY` - Django secret key (optional, has default)

### Gemini API Settings

The application is configured with the following Gemini API settings:

- Model: `gemini-1.5-flash-latest`
- Temperature: 0.7
- Max Output Tokens: 500
- Safety settings: Block medium and above harmful content

## Security Notes

- Never commit your `.env` file to version control
- The `.env` file is already included in `.gitignore`
- Keep your API keys secure and rotate them regularly
- For production deployment, use proper environment variable management

## Troubleshooting

### Common Issues

1. **"API key not configured" error**

   - Make sure you've added your Gemini API key to the `.env` file
   - Ensure the `.env` file is in the project root directory

2. **"Module not found" errors**

   - Run `pip install -r requirements.txt` to install all dependencies

3. **Server won't start**

   - Make sure you're in the correct directory (`ai_chatbot/`)
   - Check that Python and Django are properly installed

4. **API requests failing**
   - Verify your Gemini API key is valid and active
   - Check your internet connection
   - Ensure you haven't exceeded API rate limits

## Development

To extend or modify the chatbot:

1. **Frontend changes**: Edit `frontend/templates/home_page.html`
2. **Backend logic**: Modify `frontend/views.py`
3. **API configuration**: Update settings in `call_ai_model()` function
4. **Styling**: Modify the CSS in the HTML template

## Deployment

### Render Deployment

1. **Connect your repository to Render**

   - Push your code to GitHub/GitLab
   - Connect your repository to Render

2. **Configure Environment Variables in Render**

   - Go to your Render dashboard
   - Select your service
   - Navigate to **Environment** → **Environment Variables**
   - Add the following environment variable:
     - **Key**: `GEMINI_API_KEY`
     - **Value**: Your actual Gemini API key

3. **Deploy**
   - Render will use the `render.yaml` configuration
   - The build script will handle dependencies and migrations

### Important Notes for Render Deployment

- **Environment Variables**: Render reads environment variables from the dashboard. Add your API key there.
- **API Key Security**: Never commit your actual API key to your repository. Use environment variables instead.
- **Database**: This project uses SQLite which is suitable for development. For production, consider using a proper database service.

## License

This project is open source and available under the MIT License.
