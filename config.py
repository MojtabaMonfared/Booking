import re, random, string, os, sys, redis, qrcode, glob
from flask import Flask
import sqlite3 as lite
app = Flask(__name__)
redis = redis.Redis()
con = lite.connect('boooks.db')


num = 1
with con:
	cur = con.cursor()    
	cur.execute("CREATE TABLE Boooks_testt(Id INT, Title TEXT)")
	print "table created and executed! going to insert data"

while num < 4:
	i = glob.glob("books/*.pdf")
	for title in i:
		print "data %s added" % num
		cur.execute("INSERT INTO Boooks_testt VALUES({},'%{}')".format(num , title))
		num = num + 1
