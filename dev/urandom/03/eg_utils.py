from os.path import expanduser
import re
import sqlite3
from urllib import request


def get_login_cookie():
    COOKIES = expanduser("~/.mozilla/firefox/8g2pi1tn.default/cookies.sqlite")
    QUERY = "SELECT baseDomain, name, value "
    QUERY += "FROM moz_cookies "
    QUERY += "WHERE name = 'enigmafiedV4' and baseDomain = 'enigmagroup.org';"
    conn, data = None, None
    try:
        conn = sqlite3.connect(COOKIES)
        cur = conn.cursor()
        cur.execute(QUERY)
        data = cur.fetchone()
    except lite.Error as e:
        print(e.args)
        data = None
    finally:
        if conn:
            conn.close
    if data is None:
        return ()
    return ('Cookie', data[1] + '=' + data[2])
