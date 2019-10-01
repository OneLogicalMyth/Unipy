from unipy import unipy
import json, random, sys, requests

# variables
guest_wlan = 'the hex id _id you can get that from this web address https://127.0.0.1:8443/api/s/default/rest/wlanconf/'
url = 'https://127.0.0.1:8443'
wordlist = 'words.txt'
username = ''
password = ''
webhook_url = 'https://hooks.slack.com/services/AAAAAAAAA/AAAAAAAAA/AAAAAAAAAAAAAAAAAAAAAAAA'

print "[-] Loading wordlist to generate new wireless password: {}".format(wordlist)
lines = open(wordlist).read().splitlines()
guest_password = random.choice(lines) + "-" + random.choice(lines) + "-" + random.choice(lines)

print "[-] Logging into unifi controller {}".format(url)
u = unipy(url)
if not u.login(username, password):
    print "[!] Failed to login to the unifi controller {}".format(url)
    sys.exit("Unifi controller failed login.")

print "[+] Logged in successfully to the unifi controller {}".format(url)
wlan_info = u.get_wlansettings(guest_wlan)
print "[-] Current wireless password is {}".format(wlan_info["data"][0]["x_passphrase"])

print "[-] Setting wireless password to {}".format(guest_password)
new_pass = {"x_passphrase":guest_password}
if u.set_wlansettings_base(guest_wlan, new_pass):
    print "[+] Wireless password updated"

print "[-] Sending notification to Slack channel"
slack_data = {'text': "*Current Guest Wireless Password*\n`{}`".format(guest_password) }
response = requests.post(webhook_url, json=slack_data)
if response.status_code == 200:
    print "[+] Slack notification sent OK"
else:
    print "[!] Failed to notify Slack"

print "[*] All Complete!"
