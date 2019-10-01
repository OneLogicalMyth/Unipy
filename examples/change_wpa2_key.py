from unipy import unipy
import json

# variables
guest_wlan = 'hex string of _id'
guest_password = { "x_passphrase": "some new password" }

# url and creds. Can set a site name as a second param
u = unipy('https://127.0.0.1:8443')
print u.login('username','password')

# change password for wireless
print json.dumps(u.set_wlansettings_base(guest_wlan, guest_password))
