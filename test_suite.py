import requests
import sys

def main():
    URL = sys.argv[1]
    response = requests.get(URL)

    if response:
        print('OK')
    else:
        print('ERROR')

if __name__ == "__main__":
    main()
