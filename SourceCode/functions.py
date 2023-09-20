
import random


def roll_d6() -> int:
    return random.randint(1,6)

def get_d6_img(n: int) -> str:
    # desde url
    # return f"https://github.com/bormolina/bormolina.github.io/blob/main/assets/d6_{n}_sd.webm"
    # desde local path
     image_path = f"images/d6_{n}_sd.gif"
     return image_path

def get_url_flag(country: str) -> str:
    url = f'https://flagsapi.com/{country}/flat/64.png'
    return url
