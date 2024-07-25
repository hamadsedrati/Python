import requests
import colorama as cl
cl.init()


def download_image():
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

    extension = img_url.split(".")[-1]

    img_name = input(
        f"[{green}+{reset}] Enter the image name: ") + "." + extension

    if not img_name:
        print(f"[{red}ERROR{reset}] Image name cannot be empty.")
        exit()

    # Check if the image name contains any spaces
    if ' ' in img_name:
        print(f"[{red}ERROR{reset}] Image name cannot contain spaces.")
        exit()

    # Check if the image name ends with a period
    if img_name.endswith('.'):
        print(f"[{red}ERROR{reset}] Image name cannot end with a period.")
        exit()

    path = input(
        f"[{green}+{reset}] Where do you want to save the file? (full path): ")
    response = requests.get(img_url)

    if response.status_code != 200:
        print(f"[ {red}ERROR{reset} ] please check the URL and try again!")
        exit()

    print(f"[{green}+{reset}] Downloading...")
    try:
        with open(f"{path}{img_name}", "wb") as image:
            image.write(response.content)
    except FileNotFoundError:
        print(f"[ {red}ERROR{reset} ] please check the path and try again!")


download_image()
