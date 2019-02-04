
#!/usr/bin/env python

import requests
import sys
subdirectries = []
def request(url):
    try:
        get_response = requests.get(url)
        return get_response
    except Exception:
        pass


# target_url = "192.168.0.105/mutillidae"
target_url = "http://ajwapaste.com.pk"
# response = request(target_url)

# print(response)
with open("dirs.txt","r") as wordlist_file:
    subdirectories_count = 0
    for line in wordlist_file:
        word = line.strip()
        test_url =target_url + "/" + word
        response = request(test_url)
        # print(response.url + " --> "+ str(response.status_code))
        if response:
            subdirectories_count = subdirectories_count + 1
            print("\r[+] URL No. "+str(subdirectories_count))
            print("[+] Discoverd URL --> " + response.url)
            subdirectries.append(response.url)
            # \r means always start from the start of the line
            # print("\r[+] URL No. "+str(subdirectories_count)),

            # sys.stdout.flush()

    print(subdirectries)
