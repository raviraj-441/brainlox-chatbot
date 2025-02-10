# Brainlox Technical Courses Chatbot

A custom chatbot API for querying Brainlox technical courses using LangChain and Flask.

## Features
- Web scraping of Brainlox technical courses
- Vector embeddings using HuggingFace models
- Groq API integration for fast LLM responses
- Structured response formatting
- Source citation for answers

## Setup

### Prerequisites
- Python 3.9+
- Groq API key (free from [Groq Cloud](https://console.groq.com))

### Installation

1. Clone repository:
```bash
git clone https://github.com/raviraj-441/brainlox-chatbot.git
cd brainlox-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables:
```bash
export GROQ_API_KEY="your-groq-api-key"
```

4. Data ingestion:
```bash
python ingest.py
```

5. Start Flask server:
```bash
python app.py
```

## Usage

### API Endpoint
`POST http://localhost:5000/chat`

### Request Format
```json
{
    "query": "your question about Brainlox courses"
}
```

### Example Request
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What Python courses are available?"}'
```

### Example Response
```json
{
  "answer": "There are several Python courses available, including:\n\n1. PYTHON PROGRAMMING-BEGINNER (16 lessons, $30 per session) - This course is for beginners and covers the basics of Python programming.\n2. PYTHON PROGRAMMING-INTERMEDIATE (16 lessons, $35 per session) - This course is for those who already have a basic understanding of Python and want to take their skills to the next level.\n3. PYTHON PROGRAMMING-ADVANCE (30 lessons, $30 per session) - This course is for those who already know the basics of Python and want to learn advanced concepts.\n4. PYTHON PROGRAMMING GROUP CLASSES - BEGINNER - This course is a group class for beginners, but the number of lessons and price are not specified.\n5. Python Playground: Create a Hangman Game (8 lessons, $30 per session) - This course is a hands-on introduction to Python programming where you create a Hangman game.\n6. Game development using python - The details of this course are not specified.\n\nAdditionally, there are courses that use Python in specific contexts, such as:\n- AI in Stock Market Success: Career Growth Camp !! (10 lessons, $30 per session) - This course uses AI and Python to predict stock prices.\n- From Beginner to AI Pro: Kickstart Your Journey With Artificial Intelligence! (For Kids) (20 lessons, $30 per session) - This course introduces kids to AI using Python.\n- Artificial Intelligence Adventures: Building AI Chatbot Like Chatgpt (For Kids) (10 lessons, $30 per session) - This course teaches kids how to build AI chatbots using Python.",
  "sources": [
    {
      "description": "Your one stop education destination!",
      "language": "zxx",
      "source": "https://brainlox.com/courses/category/technical",
      "title": "Brainlox: Learn technical courses."
    },
    {
      "description": "Your one stop education destination!",
      "language": "zxx",
      "source": "https://brainlox.com/courses/category/technical",
      "title": "Brainlox: Learn technical courses."
    },
    {
      "description": "Your one stop education destination!",
      "language": "zxx",
      "source": "https://brainlox.com/courses/category/technical",
      "title": "Brainlox: Learn technical courses."
    },
    {
      "description": "Your one stop education destination!",
      "language": "zxx",
      "source": "https://brainlox.com/courses/category/technical",
      "title": "Brainlox: Learn technical courses."
    }
  ]
}
```

## Architecture
1. **Data Ingestion**: Web scraping using LangChain WebBaseLoader
2. **Embeddings**: HuggingFace sentence-transformers/all-MiniLM-L6-v2
3. **Vector Store**: ChromaDB for local storage
4. **LLM**: Groq/llama-3.3-70b-versatile for inference
5. **API**: Flask REST endpoint for queries

## License
MIT License