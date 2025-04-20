import json
import os
from datetime import datetime

DATA_FILE = "Blog/data/posts.json"

def read_posts():
    # Create folder if it doesn't exist
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    # If file doesn't exist create it with empty list
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
    
    # Read file
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_posts(posts):
    # Create folder if it doesn't exist
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    # Write file
    with open(DATA_FILE, "w") as f:
        json.dump(posts, f, indent=4)

def create_post(title, content, author="Admin" ): # Default admin
    posts = read_posts()
    if posts: 
        new_id = posts[-1]["id"] + 1
    else:
        new_id = 1
    new_post = {
        "id": new_id,
        "title": title,
        "content": content,
        "author": author,
        "date": datetime.now().strftime("%d %B %Y %H:%M")
    }
    posts.append(new_post)
    write_posts(posts)
    return new_post # ?

def delete_post(post_id):
    posts = read_posts()
    # Adds articles other than the deleted article
    posts = [post for post in posts if post["id"] != post_id] # ?
    write_posts(posts)
