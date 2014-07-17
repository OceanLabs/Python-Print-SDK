import requests as r
import json


public_key =
secret_key = 

passcode = {"Authorization": "ApiKey {}:{}".format(public_key, secret_key),
            "Content-Type": "application/json"}

class template:
    
    def __init__(self, passcode)

        self.blob = r.get(URL, passcode).json()
        cost = self.blob[5]
        #ect.

    def commit(self, identifier, yada):
        """Allows for commiting single changes to the template"""

        self.blob[identifier] = yada
                
        r.post(URL, self.blob[identifier], passcode)





##    def _headers(self):
##        return {
##            "Authorization": "ApiKey {}:{}".format(self.public_key, self.secret_key),
##            "Content-Type": "application/json",
##        }
##
##    def _get_request(self, url, params=None):
##        url = os.path.join(self.base_url, url)
##        r = requests.get(url, headers=self._headers)
##        return r.json()
##
##    def _post_request(self, url, data):
##        url = os.path.join(self.base_url, url)
##        r = requests.post(url, data=data, headers=self._headers)
##        return r.json()
