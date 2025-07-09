import requests

def post(long):
    response = requests.post(f"http://127.0.0.1:8000/post?long={long}") 
    return response.json()
    
def get(short):
    response = requests.get(f"http://127.0.0.1:8000/{short}")
    return response.json()

