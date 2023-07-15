import time, sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from mylib.scraping.src import tokyo_tenniscoat_mac  as mac_ver

def main():
    #initialize
    result = mac_ver.tokyo_tenniscoat()
    while(result):
        time.sleep(300)
        result = mac_ver.tokyo_tenniscoat(result)

if __name__ == "__main__":
    main()
