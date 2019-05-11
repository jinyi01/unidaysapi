# Unofficial UNiDAYS API wrapper

Used to access UNiDAY discount codes


Quick start
-----------
Requests must be installed

Login
```
u = Uniday()
u.login(email, password)
```

Once logged in codes can be retrieved by linking their pages.
The domain and code partner is critical for the URL:
> /CA/en-CA/partners/**name** 
```
code1 = u.get_code("www.myunidays.com/CA/en-CA/partners/nike/access/online")
code2 = u.get_code("https://www.myunidays.com/CA/en-CA/partners/underarmour/view/online")
```

Code reissue dates can be retrieved.
```
reissue_date = u.get_reissue("www.myunidays.com/CA/en-CA/partners/nike/access/online")
```
