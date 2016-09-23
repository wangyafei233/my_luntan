#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib.request
import http.cookiejar


def schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


url = "http://192.168.124.74/cgi/login.cgi?name=ADMIN&pwd=ADMIN"
url2 = 'http://192.168.124.74/cgi/url_redirect.cgi?url_name=sess_atraejzxeqgblfzl&url_type=jwsk'

cj = http.cookiejar.LWPCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

req = urllib.request.Request(url)
operate = opener.open(req)
local = "C:\\Users\\peter\\Desktop\\launch2.jnlp"
urllib.request.urlretrieve(url2, local, schedule)
