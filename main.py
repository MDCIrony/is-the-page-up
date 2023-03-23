from dotenv import dotenv_values
import requests
import time
from typing import Dict

# Dotenv values
config: Dict[str, str | None] = dotenv_values(".env")


def check_website_status():
    url = config["URL"]
    try:
        response = requests.get(url)
        return response.status_code == requests.status_codes.codes.ok
    except requests.exceptions.RequestException:
        return False


if __name__ == "__main__":
    while True:
        if check_website_status():
            print(
                "La página está en línea; corroborando estado nuevamente en 1 minuto."
            )
        else:
            print("La página no está en línea. Reintentando en 1 minuto.")

        time.sleep(60)
