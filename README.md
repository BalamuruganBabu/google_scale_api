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
