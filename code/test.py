import ts3

a = 0

with ts3.query.TS3Connection("localhost") as ts3conn:
	ts3conn.login(
		client_login_name="***REMOVED***",
		client_login_password="***REMOVED***"
	)
	ts3conn.use(sid=1)
	while a != 22:
		a = a + 1
		ts3conn.servergroupadd(name="LOL "+str(a))