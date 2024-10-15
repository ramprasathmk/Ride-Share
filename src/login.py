import cgi
import cgitb
import pymysql

cgitb.enable(display=1, logdir="D:/xampp/apache/logs")  # Logs errors in this directory

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
        <form action="" method="post">
            <div class="form-group">
                <label for="login-username">Username:</label>
                <input type="text" id="login-username" name="username" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="login-password">Password:</label>
                <input type="password" id="login-password" name="password" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
        </form>
        <p class="mt-3">Don't have an account? <a href="signup.py">Sign up here</a>.</p>
    </div>
</body>
</html>
''')


# Database connection setup
db_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="ridesharing",
)

cursor = db_connection.cursor()
form = cgi.FieldStorage()

# Check if form was submitted
if "username" in form and "password" in form:
    Username = form.getvalue("username")
    Password = form.getvalue("password")

    # Secure parameterized query to avoid SQL injection
    q = """SELECT Id FROM users WHERE Username=%s and Password=%s"""
    cursor.execute(q, (Username, Password))
    user = cursor.fetchone()

    # If user is found, redirect to dashboard
    if user is not None:
        user_id = user[0]
        print(f"""<script>alert('Login Successful!');location.href="dashboard.py?id={user_id}";</script>""")
    else:
        print("<script>alert('Invalid username or password. Please try again.');</script>")

# Close the connection
cursor.close()
db_connection.close()
