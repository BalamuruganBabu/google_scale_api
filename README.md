# linkly
Simulates URL Shortener, Rate Limiter, and Message Queue using Flask

# linkly Simulation

This is a backend Flask project that simulates scalable services like:

- ✅ URL Shortener
- ✅ Rate Limiter
- ✅ Message Queue

These features mimic real-world services like Bit.ly, API throttling, and background task queues.

---

## 🚀 Features

### 🔗 URL Shortener
Convert long URLs into short, unique codes and redirect using `/u/<code>`.

### ⏳ Rate Limiter
Limit client requests to a fixed number per minute using IP-based tracking.

### 📬 Message Queue
Simulate a First-In-First-Out (FIFO) task queue with enqueue and dequeue operations.

---

## 📦 Tech Stack

- Python 3
- Flask
- Postman (for testing)
- Git & GitHub

---

## 🛠️ Installation and Run

```bash
# Clone the repository
git clone https://github.com/USERNAME/linkly.git
cd linkly

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
App will start at: http://127.0.0.1:5000

🧪 Sample API Endpoints
1. Shorten URL
POST /shorten
Body (JSON):

json
Copy
Edit
{
  "url": "https://www.google.com"
}
2. Redirect
GET /u/<shortcode>

3. Enqueue Message
POST /enqueue
Body (JSON):

json
Copy
Edit
{
  "message": "Hello, World!"
}
4. Dequeue Message
GET /dequeue

🙌 Author
Balamurugan Babu

🌟 License
This project is open-source and free to use for educational purposes.
=======
[![Render](https://img.shields.io/badge/Deployed%20on-Render-00c7b7?style=for-the-badge&logo=render&logoColor=white)](https://linkly-42wo.onrender.com)
# linkly
Simulates URL Shortener, Rate Limiter, and Message Queue using Flask

# linkly Simulation

This is a backend Flask project that simulates scalable services like:

- ✅ URL Shortener
- ✅ Rate Limiter
- ✅ Message Queue

These features mimic real-world services like Bit.ly, API throttling, and background task queues.

---

## 🚀 Features

### 🔗 URL Shortener
Convert long URLs into short, unique codes and redirect using `/u/<code>`.

### ⏳ Rate Limiter
Limit client requests to a fixed number per minute using IP-based tracking.

### 📬 Message Queue
Simulate a First-In-First-Out (FIFO) task queue with enqueue and dequeue operations.

## 🗃️ Database - SQLite Integration
This project uses **SQLite** with SQLAlchemy ORM to persist URL data such as original URLs and their corresponding short codes.

### How It Works:
- When a URL is shortened via the `/shorten` endpoint, the original URL and a randomly generated short code are saved to `linkly.db` using SQLAlchemy.
- On accessing `/u/<short_code>`, the app looks up the original URL from the SQLite database and redirects the user.

### Schema:
```python
class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)

---

## 📦 Tech Stack

- Python 3
- Flask
- Postman (for testing)
- Git & GitHub

---

## 🛠️ Installation and Run

```bash
# Clone the repository
git clone https://github.com/USERNAME/linkly.git
cd linkly

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
App will start at: http://127.0.0.1:5000

🧪 Sample API Endpoints
1. Shorten URL
POST /shorten
Body (JSON):

json
Copy
Edit
{
  "url": "https://www.google.com"
}
2. Redirect
GET /u/<shortcode>

3. Enqueue Message
POST /enqueue
Body (JSON):

json
Copy
Edit
{
  "message": "Hello, World!"
}
4. Dequeue Message
GET /dequeue

🙌 Author
Balamurugan Babu

🌟 License
This project is open-source and free to use for educational purposes.

