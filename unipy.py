from requests import Session
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class unipy(object):

    def __init__(self,url):
        self.url = url

    def login(self,username,password):
        self.unifi = Session()
        login_data = { "username":  username , "password": password }
        response = self.unifi.post(self.url + '/api/login', json=login_data, verify=False)
        return response.status_code

    def get_dashboard(self):
        response = self.unifi.get(self.url + '/api/s/default/stat/dashboard', verify=False)
        return response.text

