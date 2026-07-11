import requests
import urllib.parse
import random

user_prompt="A vibrant Pixar-style 3D render of a young Indian boy sitting at a cozy wooden table, eating a steaming bowl of curly Maggi noodles. He is wearing a bright t-shirt with the name Kunal clearly and boldly printed on the front. Right next to him on the table is a cute, fluffy tabby cat enthusiastically slurping a long Maggi noodle from a smaller matching bowl. The scene features warm afternoon vibes, with golden sunlight streaming through a nearby window, creating cinematic lighting. Highly detailed, joyful expressions."
safe_prompt = urllib.parse.quote(user_prompt)
seed = random.randint(1, 100000)

url=f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}"

print(f"Generating for: {user_prompt}")

response=requests.get(url)

print(response)

if response.status_code==200:
    with open("GOAT.png","wb") as file:
        file.write(response.content)
    print("Success")
else:
    print("ERROR")