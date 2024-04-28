f=open(r"c:\Windows\System32\Drivers\etc\hosts",'r+')
# we used r before the file path to include \
website=["instagram.com","www.instagram.com"]
content=f.read()
for w in website:
    if w in content:
        '''we did this to avoid duplication of website
        incase if website is present'''
        pass
    else:
        f.write("127.0.0.1"+" "+w+"\n")