@echo off
:: Check if Git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo Git is not installed. Please install Git and try again.
    exit /b
)

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    exit /b
)

:: Clone the GitHub repository
echo Cloning the Ride-Share repository...
git clone https://github.com/ramprasathmk/Ride-Share.git

:: Navigate to the repository directory
cd Ride-Share

:: Create a virtual environment in "env" folder
echo Creating virtual environment...
python -m venv rs_env

:: Check if requirements.txt exists
if not exist requirements.txt (
    echo requirements.txt file not found. Skipping package installation.
) else (
    echo Installing packages from requirements.txt...
    rs_env\Scripts\pip install -r requirements.txt
)

:: Activate the virtual environment
echo Activating virtual environment...
if "%ComSpec%"=="" (
    rs_env\Scripts\Activate
) else (
    call rs_env\Scripts\Activate
)

echo Virtual environment is activated.