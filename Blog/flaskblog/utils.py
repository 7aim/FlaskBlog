import json
import os
from datetime import datetime

DATA_FILE = "flaskblog/data/posts.json"

def read_posts():
    # Klasör yoksa oluştur
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    # Dosya yoksa boş liste ile oluştur
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
    
    # Dosyayı oku
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_posts(posts):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)  # Klasör garantisi
    with open(DATA_FILE, "w") as f:
        json.dump(posts, f, indent=4)

def create_post(title, content, author="Admin"):
    posts = read_posts()
    new_id = posts[-1]["id"] + 1 if posts else 1
    new_post = {
        "id": new_id,
        "title": title,
        "content": content,
        "author": author,
        "date": datetime.now().strftime("%d %B %Y %H:%M")
    }
    posts.append(new_post)
    write_posts(posts)
    return new_post

def delete_post(post_id):
    posts = read_posts()
    posts = [post for post in posts if post["id"] != post_id]
    write_posts(posts)