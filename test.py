#!/usr/bin/python
from db.mtsql import sql

s = sql()

print s.get_last_3h()
