from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_url = "https://api.npoint.io/7249457ee7f003f58750"
response = requests.get(url=blog_url)
all_posts = response.json()
post_objects = []
for post in all_posts:
    post_obj = Post(post)
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/posts/int:<blog_id>')
def post(blog_id):
    requested_post = None
    for entry in post_objects:
        if entry.id == int(blog_id):
            requested_post = entry
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
