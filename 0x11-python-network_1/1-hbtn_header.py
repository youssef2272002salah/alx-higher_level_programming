#!/usr/bin/python3
''' function to fetch a url '''
import sys
from urllib.request import urlopen
if __name__ == "__main__":

    url = sys.argv[1]

    with urlopen(url) as response:
        request_id = response.getheader('X-Request-ID')
        print(request_id)
