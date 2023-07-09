import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from mylib.scraping.src import tokyo_tenniscoat_mac  as mac_ver

def main():
    mac_ver.tokyo_tenniscoat()


if __name__ == "__main__":
    main()
