import requests
import json

posts = 'https://jsonplaceholder.typicode.com/posts'
users = 'https://jsonplaceholder.typicode.com/users'
comments = 'https://jsonplaceholder.typicode.com/comments'

def get_user_id(username):
    parameter = {"username": username}
    res = requests.get(users, parameter)
    response = res.json()
    id = (response[0])["id"]
    return id

def get_posts_id(user_id):
    parameter = {"userId": user_id}
    res = requests.get(posts, parameter)
    response = res.json()
    list_of_ids = []
    for dictionary in response:
        list_of_ids.append(dictionary["id"])
    return list_of_ids

def get_emails(list_of_ids):
    res = requests.get(comments)
    response = res.json()
    emails = []
    for id in list_of_ids:
        for comment in response:
            if comment["postId"] == id:
                temp = comment["email"]
                if len(emails) == 0:
                    emails.append(temp)
                if not temp in emails:
                    emails.append(temp)
    return emails


if __name__ == "__main__":
    user_id = get_user_id('Bret')
    posts_ids = get_posts_id(user_id)
    required_emails = get_emails(posts_ids)
    print(required_emails)




