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
    <title>Sign Up Page</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        * {
            background-color: none;
            background: none;
        }
        h1 {
            text-align: center;
        }
    </style>
</head>
<body>
    <header class="bg-primary text-white text-center py-3">
        <h1>Sign Up Here &downarrow;</h1>
    </header>

    <div class="container mt-5">
        <h2>Sign Up</h2>
        <form method="post">
            <!-- Name -->
            <div class="form-group">
                <label for="signup-name">Name:</label>
                <input type="text" name="name" id="name" class="form-control" required>
            </div>
            <!-- Phone -->
            <div class="form-group">
                <label for="signup-phone">Phone:</label>
                <input type="number" name="phone" id="phone" class="form-control" required>
            </div>
            <!-- DOB -->
            <div class="form-group">
                <label for="signup-dob">DOB:</label>
                <input type="text" name="dob" id="dob" class="form-control" required>
            </div>
            <!-- Address -->
            <div class="form-group">
                <label for="signup-address">Address:</label>
                <input type="text" name="address" id="address" class="form-control" required>
            </div>
            <!-- City -->
            <div class="form-group">
                <label for="signup-city">City:</label>
                <input type="text" name="city" id="city" class="form-control" required>
            </div>
            <!-- Email -->
            <div class="form-group">
                <label for="signup-email">Email:</label>
                <input type="email" name="email" id="email" class="form-control" required>
            </div>
            <!-- Username -->
            <div class="form-group">
                <label for="signup-username">Username:</label>
                <input type="text" name="username" id="username" class="form-control" required>
            </div>
            <!-- Password -->
            <div class="form-group">
                <label for="signup-password">Password:</label>
                <input type="password" name="password" id="password" class="form-control" required>
            </div>
            <!-- User Type -->
            <div class="form-group">
                <label for="signup-usertype">User Type:</label>
                <select name="usertype" id="usertype" class="form-control" required>
                    <option value="">Select</option>
                    <option value="rider">Rider</option>
                    <option value="sharer">Sharer</option>
                </select>
            </div>
            <!-- Sign-Up Button -->
            <button type="submit" name="submit" id="submit" class="btn btn-primary btn-block">Sign Up</button>
        </form>
        <p class="mt-3">Already have an account? <a href="login.py">Login here</a>.</p>
    </div>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3">
        <p>&copy; 2024 All Rights Reserved | Ride Sharing</p>
    </footer>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
''')

# For Showing Error
cgitb.enable()

# Database connection
conn = pymysql.connect(host='localhost', user='root', password='', database='ridesharing')

# cursor
cur = conn.cursor()

# Sign-Up Form
form = cgi.FieldStorage()

# sign-up fields
Name = form.getvalue('name')
Phone = form.getvalue('phone')
Dob = form.getvalue('dob')
Address = form.getvalue('address')
City = form.getvalue('city')
Email = form.getvalue('email')
Username = form.getvalue('username')
Password = form.getvalue('password')
Usertype = form.getvalue('usertype')

try:
    q = '''INSERT INTO users(Name, Phone, DOB, Address, City, Email, Username, Password, Usertype) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')'''
    cur.execute(q, (Name, Phone, Dob, Address, City, Email, Username, Password, Usertype))
    conn.commit()
    print('''<script>alert('Your Details Registered Successfully'); location.href="signup.py"</script>''')

except pymysql.MySQLError as e:
    print(f'<script>alert("Error: {e}"); window.location.href="signup.py";</script>')

finally:
    if conn:
        conn.close()
