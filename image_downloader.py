import time
import requests
import colorama as cl
from time import sleep  # noqa F401

cl.init()


red = cl.Fore.RED
white = cl.Fore.WHITE
green = cl.Fore.GREEN
yellow = cl.Fore.YELLOW
light_yellow = cl.Fore.LIGHTYELLOW_EX
reset = cl.Fore.RESET

banner = """
   ______  ________  ___  ____ _      ___  ____   ____  ___   ___  _______ 
  /  _/  |/  / ___/ / _ \\/ __ \\ | /| / / |/ / /  / __ \\/ _ | / _ \\/ __/ _ \\
 _/ // /|_/ / (_ / / // / /_/ / |/ |/ /    / /__/ /_/ / __ |/ // / _// , _/
/___/_/  /_/\\___/ /____/\\____/|__/|__/_/|_/____/\\____/_/ |_/____/___/_/|_| 
"""
print(f"{yellow}{banner}{reset}")

help_msg = print(f"""

    1.[ {green}USAGE{reset} ] image URL: https://example.com/img.png
    2.[ {green}USAGE{reset} ] image name: example
    3.[ {green}USAGE{reset} ] path: /home/username/Desktop

""")

try:
    img_url = input(f"[{green}+{reset}] Enter the image URL: ").strip(" ")

except KeyboardInterrupt:
    print(f"\n\n[ {light_yellow}INTERRUPT{reset} ] Program stopped. Goodbye!")
    exit()

except PermissionError:
    print(
        f"\n[ {red}ERROR{reset} ] Permission denied, Please make sure that you have the required permissions and try again."
    )
    exit()


except Exception:
    print(
        f"\n[ {red}ERROR{reset} ] Unexpected error occured, please check everything is correct and try again."
    )
    exit()


if img_url.isspace() or img_url == "":
    print(
        f"\n[ {red}ERROR{reset} ] URL Required, Please enter the full URL. ex: https://example.com/image.png"
    )
    exit()


try:
    response = requests.get(img_url)

except requests.exceptions.InvalidURL:
    print(
        f"\n[ {red}ERROR{reset} ] Invalid URL, please check that the URL is correct and try again. ex: https://example.com/image.png"
    )
    exit()

except requests.exceptions.MissingSchema:
    print(
        f"\n[ {red}ERROR{reset} ] Missing Schema, Please enter the full URL. ex: https://example.com/image.png"
    )
    exit()

except requests.exceptions.InvalidSchema:
    print(
        f"\n[ {red}ERROR{reset} ] Invalid Schema, Please make sure the entered URL is correct and try again. ex: https://example.com/image.png"
    )
    exit()

except requests.ConnectionError:
    print(
        f"\n[ {red}ERROR{reset} ] Connection Error, Please check your internet connection and make sure that the URL is correct and try again. ex: https://example.com/image.png"
    )
    exit()

except requests.Timeout:
    print(
        f"\n[ {red}ERROR{reset} ] Connection Timed out, Please check your internet connection and make sure that the URL is correct and try again. ex: https://example.com/image.png"
    )
    exit()

except requests.exceptions.HTTPError:
    print(
        "An HTTP Error occured, Please try again later, or check the specified URL. ex: https://example.com/image.png"
    )
    exit()


extension = img_url.split(".")[-1]

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

proh_chars = [
    ".",
    ",",
    ":",
    "/",
    ";",
    "<",
    ">",
    "?",
    "{",
    "}",
    "[",
    "]",
    "|",
    "(",
    ")",
    "`",
    "~",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "-",
    "_",
] + nums

for i in proh_chars:
    if i in extension:
        print(
            f"\n[ {red}ERROR{reset} ] Invalid extension, please check that the image extension is correct ex: https://example.com/image(.png) "
        )
        exit()


try:
    img_name = input(f"\n[{green}+{reset}] Enter the image name: ")

except KeyError:
    print(
        f"\n[ {red}ERROR{reset} ] Unexpected error occured, please check everything is correct and try again."
    )
    exit()

except KeyboardInterrupt:
    print(f"\n[ {yellow}INTERRUPT{reset} ] Program stopped, GoodBye!")
    exit()

# check for prohibited chars for file names in the internet then put it here
proh_charsext = [
    " ",
    "#",
    "$",
    "&",
    "{",
    "}",
    "\\",
    "<",
    ">",
    "?",
    "*",
    "/",
    "!",
    "'",
    '"',
    ":",
    "@",
    "+",
    "`",
    "|",
    "=",
]

for i in proh_charsext:
    if i in img_name:
        print(
            f"\n[ {red}ERROR{reset} ] Invalid name, please check that the image name is correct ex: img_name"
        )
        exit()


if img_name.isspace() or img_name == "":
    print(f"\n[ {red}ERROR{reset} ] Image name cannot be empty.")
    exit()

if (
    img_name.startswith(" ")
    or img_name.startswith(".")
    or img_name.startswith("-")
    or img_name.startswith("_")
):
    print(
        f"\n[ {red}ERROR{reset} ] Image name cannot start with a space, period, dash, or underscore. ex: img_name"
    )
    exit()

    # Check if the image name ends with a period
if img_name.endswith(".") or img_name.endswith("." + extension):
    print(
        f"\n[ {red}ERROR{reset} ] Image name cannot end with a period/extension. ex: img_name"
    )
    exit()

img_name + "." + extension

path = input(f"\n[{green}+{reset}] Where do you want to save the file? (full path): ")

if "/" in path:
    if not path.endswith("/"):
        path = path + "/"

elif "\\" in path:
    if not path.endswith("\\"):
        path = path + "\\"

print(f"\n[{green}+{reset}] Downloading...")

try:
    with open(f"{path}{img_name}", "wb") as image:
        image.write(response.content)
        exit()

except Exception as e:  # noqa: F841
    print(
        f"\n[ {red}ERROR{reset} ] Unexpected error occured, please check everything is correct and try again."
    )

except KeyboardInterrupt:
    print(f"\n\n[ {yellow}INTERRUPT{reset} ] Program Stopped, Goodbye!")

finally:
    time.sleep(1)
    print(f"\n[{green}+{reset}] Done!")
    print(
        f"\n[ {yellow}help{reset} ] If the image did not download, make sure everything is right then try again. You can read the help message above."
    )
    
    print()
