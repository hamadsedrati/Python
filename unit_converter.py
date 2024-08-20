import time
import colorama as cl
from time import sleep  # noqa: F401

units = ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"]

red = cl.Fore.RED
green = cl.Fore.GREEN
blue = cl.Fore.BLUE
magenta = cl.Fore.MAGENTA
yellow = cl.Fore.YELLOW
reset = cl.Fore.RESET

cl.init()

print(f"{red}Precise Unit Converter by DrobaK{reset}")
print(
    f"\n[ {green}USAGE{reset} ] {blue}first number{reset} is the number that will be converted.\n{magenta}first numbers unit{reset} is the unit of the {blue}first number{reset} (the num that will be converted)\n"
)
print(f"{yellow}second numbers unit{reset} is the unit that you want to convert to.\n")

try:
    first_num = int(input(f"{blue}First Number{reset}: "))
except ValueError:
    print(f"[ {red}ERROR{reset} ] Please enter a number")
    exit()

except KeyboardInterrupt:
    print(f"\n\n[ {yellow}INTERRUPT{reset} ] Program Stopped, Goodbye!")
    exit()

except Exception:
    print(
        f"[ {red}ERROR{reset} ] Unexpected error, Please check your inputs and try again. If the issue persists, contact me."
    )


first_num_unit = input(f"{magenta}first numbers unit{reset}: ").lower()

if first_num_unit not in units:
    print(
        f"\n[ {red}ERROR{reset} ] Invalid unit, try again with one of the following units: mm, cm, m, km, in, ft, yd, mi"
    )
    exit()

second_num_unit = input(f"{yellow}second numbers unit{reset}: ").lower()


if second_num_unit not in units:
    print(
        f"\n[ {red}ERROR{reset} ] Invalid unit, try again with one of the following units: mm, cm, m, km, in, ft, yd, mi"
    )
    exit()

if first_num_unit == second_num_unit:
    print(f"\n[ {red}wtf{reset} ] are you retarded or smthn?")
    exit()


def mm_to_cm():
    if first_num_unit == "mm" and second_num_unit == "cm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 10, "cm")


def mm_to_m():
    if first_num_unit == "mm" and second_num_unit == "m":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 1000, "m")


def mm_to_km():
    if first_num_unit == "mm" and second_num_unit == "km":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 1000000, "km")


def mm_to_in():
    if first_num_unit == "mm" and second_num_unit == "in":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num_unit / 25.4, "in")


def mm_to_ft():
    if first_num_unit == "mm" and second_num_unit == "ft":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num_unit / 304.8, "ft")


def mm_to_yd():
    if first_num_unit == "mm" and second_num_unit == "yd":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num_unit / 914.4, "yd")


def mm_to_mi():
    if first_num_unit == "mm" and second_num_unit == "mi":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num_unit / 1609344, "mi")


def cm_to_mm():
    if first_num_unit == "cm" and second_num_unit == "mm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 10, "mm")


def cm_to_m():
    if first_num_unit == "cm" and second_num_unit == "m":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 100, "m")


def cm_to_km():
    if first_num_unit == "cm" and second_num_unit == "km":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 100000, "km")


def cm_to_in():
    if first_num_unit == "cm" and second_num_unit == "in":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 2.54, "in")


def cm_to_ft():
    if first_num_unit == "cm" and second_num_unit == "ft":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 30.48, "ft")


def cm_to_yd():
    if first_num_unit == "cm" and second_num_unit == "yd":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 91.44, "yd")


def cm_to_mi():
    if first_num_unit == "cm" and second_num_unit == "mi":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 160934.4, "mi")


def m_to_mm():
    if first_num_unit == "m" and second_num_unit == "mm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 1000, "mm")


def m_to_cm():
    if first_num_unit == "m" and second_num_unit == "cm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 100, "cm")


def m_to_km():
    if first_num_unit == "m" and second_num_unit == "m":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 100, "km")


def m_to_in():
    if first_num_unit == "m" and second_num_unit == "in":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 0.0254, "in")


def m_to_ft():
    if first_num_unit == "m" and second_num_unit == "ft":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 0.3048, "ft")


def m_to_yd():
    if first_num_unit == "m" and second_num_unit == "yd":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 0.9144, "yd")


def m_to_mi():
    if first_num_unit == "m" and second_num_unit == "mi":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num / 1609.344, "mi")


def km_to_mm():
    if first_num_unit == "km" and second_num_unit == "mm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 1000000, "mm")


def km_to_cm():
    if first_num_unit == "km" and second_num_unit == "cm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 100000, "cm")


def km_to_m():
    if first_num_unit == "km" and second_num_unit == "m":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 1000, "m")


def km_to_in():
    if first_num_unit == "km" and second_num_unit == "in":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 39370.1, "in")


def km_to_ft():
    if first_num_unit == "km" and second_num_unit == "ft":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 3280.84, "ft")


def km_to_yd():
    if first_num_unit == "km" and second_num_unit == "yd":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 1093.61, "yd")


def km_to_mi():
    if first_num_unit == "km" and second_num_unit == "mi":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.621371, "mi")


def in_to_mm():
    if first_num_unit == "in" and second_num_unit == "mm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 25.4, "mm")


def in_to_cm():
    if first_num_unit == "in" and second_num_unit == "cm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 2.54, "cm")


def in_to_m():
    if first_num_unit == "in" and second_num_unit == "m":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.0254, "m")


def in_to_km():
    if first_num_unit == "in" and second_num_unit == "km":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.0000254, "km")


def in_to_ft():
    if first_num_unit == "in" and second_num_unit == "ft":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.0833333, "ft")


def in_to_yd():
    if first_num_unit == "in" and second_num_unit == "yd":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.0277778, "yd")


def in_to_mi():
    if first_num_unit == "in" and second_num_unit == "mi":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.0000157828, "mi")


def ft_to_mm():
    if first_num_unit == "ft" and second_num_unit == "mm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 304.8, "mm")


def ft_to_cm():
    if first_num_unit == "ft" and second_num_unit == "cm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 30.48, "cm")


def ft_to_m():
    if first_num_unit == "ft" and second_num_unit == "m":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.3048, "m")


def ft_to_km():
    if first_num_unit == "ft" and second_num_unit == "km":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.0003048, "km")


def ft_to_in():
    if first_num_unit == "ft" and second_num_unit == "in":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 12, "in")


def ft_to_yd():
    if first_num_unit == "ft" and second_num_unit == "yd":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.333333, "yd")


def ft_to_mi():
    if first_num_unit == "ft" and second_num_unit == "mi":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.000189394, "mi")


def yd_to_mm():
    if first_num_unit == "yd" and second_num_unit == "mm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 914.4, "mm")


def yd_to_cm():
    if first_num_unit == "yd" and second_num_unit == "cm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 91.44, "cm")


def yd_to_m():
    if first_num_unit == "yd" and second_num_unit == "m":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.9144, "m")


def yd_to_km():
    if first_num_unit == "yd" and second_num_unit == "km":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.0009144, "km")


def yd_to_in():
    if first_num_unit == "yd" and second_num_unit == "in":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 36, "in")


def yd_to_ft():
    if first_num_unit == "yd" and second_num_unit == "ft":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 3, "ft")


def yd_to_mi():
    if first_num_unit == "yd" and second_num_unit == "mi":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 0.000568182, "mi")


def mi_to_mm():
    if first_num_unit == "mi" and second_num_unit == "mm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 1609344, "mm")


def mi_to_cm():
    if first_num_unit == "mi" and second_num_unit == "cm":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 160934.4, "cm")


def mi_to_m():
    if first_num_unit == "mi" and second_num_unit == "m":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 1609.344, "m")


def mi_to_km():
    if first_num_unit == "mi" and second_num_unit == "km":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 1.609344, "km")


def mi_to_in():
    if first_num_unit == "mi" and second_num_unit == "in":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 63360, "in")


def mi_to_ft():
    if first_num_unit == "mi" and second_num_unit == "ft":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 5280, "ft")


def mi_to_yd():
    if first_num_unit == "mi" and second_num_unit == "yd":
        print(f"\n[{green}+{reset}] Converting...")
        time.sleep(0.5)
        print("\n", first_num * 1760, "yd")


match first_num_unit:
    case "mm":
        mm_to_cm()
        mm_to_m()
        mm_to_km()
        mm_to_in()
        mm_to_ft()
        mm_to_yd()
        mm_to_mi()

    case "cm":
        cm_to_mm()
        cm_to_m()
        cm_to_km()
        cm_to_in()
        cm_to_ft()
        cm_to_yd()
        cm_to_mi()

    case "m":
        m_to_mm()
        m_to_cm()
        m_to_km()
        m_to_in()
        m_to_ft()
        m_to_yd()
        m_to_mi()

    case "km":
        km_to_mm()
        km_to_cm()
        km_to_m()
        km_to_in()
        km_to_ft()
        km_to_yd()
        km_to_mi()

    case "in":
        in_to_mm()
        in_to_cm()
        in_to_m()
        in_to_km()
        in_to_ft()
        in_to_yd()
        in_to_mi()

    case "ft":
        ft_to_mm()
        ft_to_cm()
        ft_to_m()
        ft_to_km()
        ft_to_in()
        ft_to_yd()
        ft_to_mi()

    case "yd":
        yd_to_mm()
        yd_to_cm()
        yd_to_m()
        yd_to_km()
        yd_to_in()
        yd_to_ft()
        yd_to_mi()

    case "mi":
        mi_to_mm()
        mi_to_cm()
        mi_to_m()
        mi_to_km()
        mi_to_in()
        mi_to_ft()
        mi_to_yd()
