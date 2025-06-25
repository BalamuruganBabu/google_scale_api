from flask import Flask, request, jsonify, redirect
from url_shortener import URLShortener
from rate_limiter import RateLimiter
from message_queue import MessageQueue

app = Flask(__name__)

url_shortener = URLShortener()
rate_limiter = RateLimiter(limit=5, window_seconds=60)
message_queue = MessageQueue()

@app.route('/shorten', methods=['POST'])
def shorten():
    if not rate_limiter.allow(request.remote_addr):
        return jsonify({"error": "Rate limit exceeded"}), 429
    long_url = request.json.get("url")
    short_code = url_shortener.shorten_url(long_url)
    return jsonify({"short_code": short_code})

@app.route('/u/<code>', methods=['GET'])
def redirect_to_url(code):
    url = url_shortener.get_url(code)
    if url:
        return redirect(url)
    return jsonify({"error": "Invalid code"}), 404

@app.route('/enqueue', methods=['POST'])
def enqueue():
    message = request.json.get("message")
    message_queue.enqueue(message)
    return jsonify({"status": "Message enqueued"})

@app.route('/dequeue', methods=['GET'])
def dequeue():
    message = message_queue.dequeue()
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
