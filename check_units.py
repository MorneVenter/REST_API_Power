import requests
from lxml import html

USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"
LOGIN_URL = "https://www.oami.co.za/clients/Login.aspx"
URL = "https://www.oami.co.za/clients/poc.aspx"

session_requests = requests.session()
result = session_requests.get(LOGIN_URL)
tree = html.fromstring(result.text)
viewstate = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
viewstategen = list(set(tree.xpath("//input[@name='__VIEWSTATEGENERATOR']/@value")))[0]
payload = {
    "__VIEWSTATE": viewstate,
    "__VIEWSTATEGENERATOR": viewstategen,
    "username": USERNAME,
    "password": PASSWORD,
    "submit": 'Login'
}
result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
result = session_requests.get(URL, headers = dict(referer = URL))
tree = html.fromstring(result.content)
units = tree.xpath('//*[@id="LblPPkwh"]/text()[last()]')
print(units[0])
