from fastapi import FastAPI

# setting up application api's
app = FastAPI()


# Sample post data in list format with id and content
text_posts = {
    1: {"title": "Getting Started with FastAPI", "content": "Learn the basics of FastAPI and build your first API."},
    2: {"title": "Python Tips and Tricks", "content": "Discover useful Python programming techniques to improve your code."},
    3: {"title": "Web Development Best Practices", "content": "Follow industry standards for building scalable web applications."},
    4: {"title": "Understanding REST APIs", "content": "Deep dive into REST principles and how to design RESTful services."},
    5: {"title": "Database Optimization", "content": "Learn strategies to optimize your database queries and performance."},
    6: {"title": "Async Programming in Python", "content": "Master asynchronous programming with asyncio and async/await."},
    7: {"title": "API Security", "content": "Implement authentication, authorization, and security best practices."},
    8: {"title": "Testing FastAPI Applications", "content": "Write unit tests and integration tests for your FastAPI endpoints."},
    9: {"title": "Deployment Strategies", "content": "Deploy your FastAPI application to production with Docker and cloud platforms."},
    10: {"title": "Microservices Architecture", "content": "Build scalable systems using microservices design patterns."}
}

# To set up new get api
@app.get("/posts")
def get_all_posts():
    return text_posts

# testing get api with id as input and return the post content
@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

# post api to add two numbers
@app.post("/add_numbers")
def add_numbers(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}
