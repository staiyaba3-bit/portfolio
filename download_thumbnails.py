import urllib.request
import os

urls = {
    "bakery-preview.jpg": "https://image.thum.io/get/width/1200/crop/800/https://my-bakery-tau.vercel.app/",
    "cafe-preview.jpg": "https://image.thum.io/get/width/1200/crop/800/https://cafe-website-five-kappa.vercel.app/",
    "gym-preview.jpg": "https://image.thum.io/get/width/1200/crop/800/https://apex-fitness-club-beryl.vercel.app/",
    "birthday-preview.jpg": "https://image.thum.io/get/width/1200/crop/800/https://birthday-website-beta-opal.vercel.app/"
}

for filename, url in urls.items():
    print(f"Downloading {filename} from {url}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
