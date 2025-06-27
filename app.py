from flask_sqlalchemy import SQLAlchemy
from models import db, URLMap
import string
import random

from flask import Flask, request, jsonify, redirect
from url_shortener import URLShortener
from rate_limiter import RateLimiter
from message_queue import MessageQueue

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///linkly.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

rate_limiter = RateLimiter(limit=5, window_seconds=60)
message_queue = MessageQueue()

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'Missing URL'}), 400

    # Check if URL already shortened
    existing = URLMap.query.filter_by(original_url=url).first()
    if existing:
        return jsonify({'short_code': existing.short_code}), 200

    # Generate unique short code
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    new_entry = URLMap(original_url=url, short_code=short_code)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({'short_code': short_code}), 201
@app.route('/u/<code>', methods=['GET'])
def redirect_url(code):
    url_entry = URLMap.query.filter_by(short_code=code).first()
    if not url_entry:
        return jsonify({'error': 'Invalid code'}), 404
    return redirect(url_entry.original_url)

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
