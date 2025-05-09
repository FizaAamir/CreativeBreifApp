# 📝 Creative Brief Generator using Gemini & SearXNG

This project automates the creation of structured, marketing-grade creative briefs using user input, brand guidelines, and live web research powered by [Gemini](https://ai.google.dev/) and [SearXNG](https://github.com/searxng/searxng).

---

## 🚀 Features

- Generates creative briefs in valid, structured JSON format.
- Enriches briefs using live web search results via SearXNG.
- Prompts a Gemini model with detailed input for quality outputs.
- Configurable brand personas, targeting, and voice guidelines.
- Extensible modular structure with config-driven behavior.

---

## 📁 Project Structure
Project/
│
├── app.py # Entry point
├── requirements.txt # Python dependencies
├── docker-compose.yml # Local SearXNG service
├── .env # API key and config
│
├── Configs/
│ ├── config.yaml # Model & search config
│ └── prompts.py # Gemini prompt template
│
├── src/
│ ├── init.py
│ ├── models.py # Pydantic models
│ ├── utils.py # Web search + generation logic
│ └── constants.py # Sample user input


---

## ⚙️ Setup Instructions

### 1. Clone & Install

```bash
git clone https://github.com/YOUR_USERNAME/creative-brief-generator.git
cd creative-brief-generator
pip install -r requirements.txt
2. Configure Environment
Create a .env file in the root:

ini
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
```

🧪 Run the App
bash
Copy
Edit
python app.py
Output: A formatted JSON creative brief will be printed based on the data and live web context.

🧼 Code Quality (Flake8)
Linting is enforced via GitHub Actions.
