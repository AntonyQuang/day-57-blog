import requests

class Post:
    def __init__(self, post_obj):
        self.id = post_obj["id"]
        self.title = post_obj["title"]
        self.subtitle = post_obj["subtitle"]
        self.body = post_obj["body"]
