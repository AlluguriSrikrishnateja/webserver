from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title>My Web Server</title>
</head>
<body>
<h1>Top five web application frameworks</h1>
<h2>1.django</h2>
<h2>2.Angluar</h2>
<h2>3.Express</h2>
<h2>4.Ruby on Rails</h2>
<h2>5.BootStrap</h2>
</body>
</html>
'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request recieved...")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content.encode())

print("this is my web server")
server_address =('',80)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()