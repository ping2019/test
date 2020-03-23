#------------line_notify.py------------
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests

url = 'https://notify-api.line.me/api/notify'
token = 'P04wLqM52wwautYZY0oDdPDhY4rXkTck8NMRlDG8Ay6'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

msg = 'ส่งข้อความ LINE Notify'
r = requests.post(url, headers=headers, data = {'message':msg})

print r.text
