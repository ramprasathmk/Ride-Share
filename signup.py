#!C:/Python311/python.exe
import cgi
import cgitb
import pymysql

print("content-type: text/html \r\n\r\n")
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h2>Sign Up</h2>
        <form action="/signup" method="post">
            <div class="form-group">
                <label for="signup-username">Username:</label>
                <input type="text" id="signup-username" name="username" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="signup-email">Email:</label>
                <input type="email" id="signup-email" name="email" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="signup-password">Password:</label>
                <input type="password" id="signup-password" name="password" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Sign Up</button>
        </form>
        <p class="mt-3">Already have an account? <a href="login.py">Login here</a>.</p>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
''')


cgitb.enable()

# Database connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='ridesharing'
)

form = cgi.FieldStorage()
username = form.getvalue('username')
email = form.getvalue('email')
password = form.getvalue('password')

if username and email and password:
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username=%s OR email=%s"
            cursor.execute(sql, (username, email))
            user = cursor.fetchall()

            if user:
                print("Username or email already exists. <a href='../signup.html'>Try again</a>")
            else:
                sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
                cursor.execute(sql, (username, email, password))
                connection.commit()
                print("Registration successful. <a href='../login.html'>Login</a>")

    except Exception as e:
        print(f"Error: {e}")

connection.close()
