





# Import the 'app' object from the 'server' module
from server import app


# Define the main function that will start the application
def main():
    # Assign the imported Flask app instance to a local variable
    flask_app_instance = app
    # Run the Flask application (starts the development server)
    flask_app_instance.run()


# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to start the app
    main()






