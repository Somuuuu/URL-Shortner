import requests

def post(long):
    response = requests.post(f"http://127.0.0.1:8000/post?long={long}") 
    return response.json()
    
def get(short):
    response = requests.get(f"https://url-shortner-5r7w-3qirap44b-somus-projects-3ca5f015.vercel.app/{short}")
    return response.json()

