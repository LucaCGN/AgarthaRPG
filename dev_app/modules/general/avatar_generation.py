import requests
import json
from PIL import Image
from io import BytesIO
from config import OPENAI_API_KEY  # Assuming OPENAI_API_KEY is defined in config.py

def fetch_character_details(global_cache):
    """
    Fetch character details from the global cache.
    """
    character_details = global_cache.get('character_details', {})
    return character_details

def generate_avatar_image(character_details):
    """
    Generate an avatar image based on the character details using the OpenAI API.
    """
    prompt = f"A {character_details.get('gender', 'unspecified')} character with {character_details.get('eye_color', 'unspecified')} eyes and {character_details.get('hair_color', 'unspecified')} hair, having a {character_details.get('body_type', 'unspecified')} body type."
    
    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "prompt": prompt,
        "n": 1,
        "size": "512x512",
        "response_format": "url"
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        image_url = response.json()["data"][0]["url"]
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        avatar_path = f"C:\\Users\\Luca\\Documents\\GITHUB\\AgarthaRPG\\dev_app\\game\\avatar\\{character_details['username']}_{character_details['character_name']}.png"
        image.save(avatar_path)
        return avatar_path
    else:
        return None

def generate_character_description(character_details):
    """
    Generate a textual description of the character using the OpenAI API.
    """
    prompt = f"Tell me more about a {character_details.get('gender', 'unspecified')} character with {character_details.get('eye_color', 'unspecified')} eyes and {character_details.get('hair_color', 'unspecified')} hair, having a {character_details.get('body_type', 'unspecified')} body type."
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return None

if __name__ == "__main__":
    global_cache = {
        'character_details': {
            'username': 'luca',
            'character_name': 'john_doe',
            'eye_color': 'blue',
            'hair_color': 'blonde',
            'gender': 'Male',
            'body_type': 'Normal'
        }
    }
    
    character_details = fetch_character_details(global_cache)
    
    avatar_path = generate_avatar_image(character_details)
    print(f"Avatar saved at: {avatar_path}")
    
    character_description = generate_character_description(character_details)
    print(f"Generated Character Description: {character_description}")
