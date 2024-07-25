import requests
import colorama as cl
cl.init()

red = cl.Fore.RED
white = cl.Fore.WHITE
green = cl.Fore.GREEN
yellow = cl.Fore.YELLOW
reset = cl.Fore.RESET

banner = '''________                       ________                       ______            _________
____  _/______ __________ _    ___  __ \________      ___________  /___________ ______  /____________
 __  / __  __ `__ \_  __ `/    __  / / /  __ \_ | /| / /_  __ \_  /_  __ \  __ `/  __  /_  _ \_  ___/
__/ /  _  / / / / /  /_/ /     _  /_/ // /_/ /_ |/ |/ /_  / / /  / / /_/ / /_/ // /_/ / /  __/  /
/___/  /_/ /_/ /_/_\__, /      /_____/ \____/____/|__/ /_/ /_//_/  \____/\__,_/ \__,_/  \___//_/
                  /____/
                  '''
print(f"{yellow}{banner}{reset}")

img_url = input(f"[{green}+{reset}] Enter the image URL: ")

try:
    response = requests.get(img_url)

except requests.exceptions.InvalidURL:
    print(f"\n[ {red}ERROR{reset} ] Invalid URL, please check the URL is correct and try again ex. https://example.com/image.png")
    exit()

except requests.exceptions.MissingSchema:
    print(
        f"\n[ {red}ERROR{reset} ] Please enter the full URL ex. https://example.com/image.png")
    exit()

except requests.ConnectionError:
    print(f"\n[ {red}ERROR{reset} ] Connection Error, Please check your internet connection and try again.")



if img_url == '':
    print(f"\n[ {red}ERROR{reset} ] Image url cannot be empty.")
    exit()

extension = img_url.split(".")[-1]

img_name = input(
    f"\n[{green}+{reset}] Enter the image name: ") + "." + extension

if img_name == '':
    print(f"\n[ {red}ERROR{reset} ] Image name cannot be empty.")
    exit()

    # Check if the image name contains any spaces
if ' ' in img_name:
    print(f"\n[ {red}ERROR{reset} ] Image name cannot contain spaces.")
    exit()

    # Check if the image name ends with a period
if img_name.endswith('.') or img_name.endswith("."+extension):
    print(f"\n[ {red}ERROR{reset} ] Image name cannot end with a period/extension.")
    exit()

path = input(
    f"\n[{green}+{reset}] Where do you want to save the file? (full path): ")


if response.status_code != 200:
    print(f"\n[ {red}ERROR{reset} ] please check the URL and try again!")
    exit()

print(f"\n[{green}+{reset}] Downloading...")

with open(f"{path}{img_name}", "wb") as image:
    image.write(response.content)
