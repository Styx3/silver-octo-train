import requests
import sys

def main():
    URL = sys.argv[1]
    response = requests.get(URL)

    if response:
        print('OK')
        return 0
    else:
        print('ERROR')
        return 1

if __name__ == "__main__":
    main()
