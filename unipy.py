from requests import Session
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class unipy(object):

    def __init__(self,url,site='default'):
        self.url = url
        self.site = site
        self.logged_in = False

    def login(self,username,password):
        self.unifi = Session()
        login_data = { "username":  username , "password": password }
        response = self.unifi.post(self.url + '/api/login', json=login_data, verify=False)

        if response.status_code == 200:
            self.logged_in = True
        else:
            self.logged_in = False

        return self.logged_in

    def get_dashboard(self):
        if not self.logged_in:
            return False
        
        response = self.unifi.get(self.url + '/api/s/' + self.site + '/stat/dashboard', verify=False)
        return response.text

    def set_wlansettings_base(self,wlan_id,payload):
        if not self.logged_in:
            return False

        response = self.unifi.put(self.url + '/api/s/' + self.site + '/rest/wlanconf/' + wlan_id, json=payload, verify=False)
        return response.text
