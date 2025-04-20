from flask import Flask, render_template, request, redirect, abort
from utils import read_posts, create_post, delete_post # ? write_posts()

app = Flask(__name__)

# Main page 
@app.route('/')
def home():
    posts = read_posts()
    return render_template('index.html', posts=posts)

# Create article
@app.route('/create', methods=['GET', 'POST']) # ? methods
def create():
    if request.method == 'POST':
        create_post(
            title=request.form['title'],
            content=request.form['content']
        )
        return redirect('/')
    return render_template('create.html')

# Article
@app.route('/post/<int:post_id>')
def post(post_id):
    posts = read_posts()
    post = next((p for p in posts if p["id"] == post_id), None) # ?
    if not post:
        abort(404)
    return render_template('post.html', post=post)

# Delete article
@app.route('/delete/<int:post_id>', methods=['GET'])
def delete(post_id):
    delete_post(post_id)
    return redirect('/') # ?

if __name__ == '__main__':
    app.run(debug=True)