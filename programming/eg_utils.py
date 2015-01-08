#!/usr/bin/env python

from os.path import expanduser
import re
import sqlite3
import urllib

def get_login_cookie():
	COOKIE_DB = expanduser("~/.mozilla/firefox/8g2pi1tn.default/cookies.sqlite")
	QUERY = "SELECT baseDomain, name, value FROM moz_cookies WHERE name = 'enigmafiedV4' and baseDomain = 'enigmagroup.org';"
	conn, data = None, None
	try:
		conn = sqlite3.connect( COOKIE_DB )
		cur = conn.cursor()
		cur.execute( QUERY )
		data = cur.fetchone()
	except lite.Error, e:
		print e.args
		data = None
	finally:
		if conn:
			conn.close
	if data == None:
		return ()
	return ('Cookie', data[1] + '=' + data[2])

def get_external_ip():
	site = urllib.urlopen("http://checkip.dyndns.org/").read()
	grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site)
	return grab[0]        
