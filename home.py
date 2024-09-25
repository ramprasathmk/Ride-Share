#!C:/Python312/python.exe
print("content-type: text/html \r\n\r\n")
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ride Sharing</title>
    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="bg-primary text-white text-center py-3">
        <h1>Ride Sharing System</h1>
    </header>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">Ride Sharing</a>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item"><a class="nav-link" href="#admin">Administrator</a></li>
                <li class="nav-item"><a class="nav-link" href="#ride-sharer">Ride Sharer</a></li>
                <li class="nav-item"><a class="nav-link" href="#ride-seeker">Ride Seeker</a></li>
                <li class="nav-item"><a class="nav-link" href="#ride-details">Ride Details</a></li>
            </ul>
            <ul>
                <li class="nav-item"> <a class=nav-link" href="login.py"> Login </a> </li>
                <li class="nav-item"> <a class=nav-link" href="signup.py"> Sign Up </a> </li>
            </ul>
        </div>
    </nav>

    <main class="container my-4">
        <section id="admin">
            <h2>Administrator</h2>
            <p>Manage users and rides. Validate seeker and sharer details.</p>
        </section>

        <section id="ride-sharer" class="mt-5">
            <h2>Ride Sharer</h2>
            <form>
                <div class="form-group">
                    <label for="sharer-name">Name:</label>
                    <input type="text" id="sharer-name" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="vehicle-details">Vehicle Details:</label>
                    <input type="text" id="vehicle-details" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-primary">Register as Sharer</button>
            </form>
        </section>

        <section id="ride-seeker" class="mt-5">
            <h2>Ride Seeker</h2>
            <form>
                <div class="form-group">
                    <label for="seeker-name">Name:</label>
                    <input type="text" id="seeker-name" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="destination">Destination:</label>
                    <input type="text" id="destination" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-primary">Find Ride</button>
            </form>
        </section>

        <section id="ride-details" class="mt-5">
            <h2>Ride Details</h2>
            <div id="rides-list">
                <!-- Ride details will be populated here -->
            </div>
        </section>
    </main>

    <footer class="bg-dark text-white text-center py-3">
        <p>&copy; 2024 Ride Sharing</p>
    </footer>

    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <!-- Custom JS -->
    <script src="script.js"></script>
</body>
</html>
''')
