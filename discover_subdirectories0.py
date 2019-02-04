
#!/usr/bin/env python

import requests

def request(url):
        get_response = requests.get(url)
        return get_response



# target_url = "192.168.0.105/mutillidae"
target_url = "http://ajwapaste.com.pk/"

response = request(target_url)
print(response)
