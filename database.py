posts = [
    {
        "id": 1,
        "title": "Meu primeiro post",
        "content": "Este é o conteúdo do primeiro post."
    },
    {
        "id": 2,
        "title": "segundo post",
        "content": "Mais conteúdo aqui."
    }
]

def get_post():
    return posts

def get_post(id):
    for post in posts:
        if str(post["id"]) == str(id):
            return post