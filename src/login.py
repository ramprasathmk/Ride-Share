#!C:/Python312/python.exe

# import cgi
# import cgitb
# import pymysql

print("content-type: text/html \r\n\r\n")
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
    <div class="container mt-5">
        <h2>Login</h2>
        <form action="/login" method="post">
            <div class="form-group">
                <label for="login-username">Username:</label>
                <input type="text" id="login-username" name="username" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="login-password">Password:</label>
                <input type="password" id="login-password" name="password" class="form-control" required>
            </div>
            <!--
            <div class="form-group">
                <label for="login-usertype">Usertype:</label>
                <input type="usertype" id="login-usertype" name="usertype" class="form-control" required>
            </div>
            -->
            <button type="submit" class="btn btn-primary">Login</button>
        </form>
        <p class="mt-3">Don't have an account? <a href="signup.py">Sign up here</a>.</p>
    </div>

    <script>
      
    </script>
</body>
</html>
''')

# For Showing Error
# cgitb.enable()
#
# # Connection
# connection = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='ridesharing'
# )
# # Cursor
# cursor = connection.cursor()
# # Form
# form = cgi.FieldStorage()
#
# # Submit
# Submit = form.getvalue("submit")
#
# # Form entities
# username = form.getvalue('username', '')
# email = form.getvalue('email', '')
# password = form.getvalue('password', '')
