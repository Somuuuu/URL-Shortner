import requests

def post(long):
    response = requests.post(f"https://url-shortner-5r7w-3qirap44b-somus-projects-3ca5f015.vercel.app/post?long={long}") 
    return response.json()
    
def get(short):
    response = requests.get(f"https://url-shortner-5r7w-3qirap44b-somus-projects-3ca5f015.vercel.app/{short}")
    return response.json()

