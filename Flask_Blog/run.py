from flaskblog import app
# imports the app instance from __init__.py from flaskblog package

if __name__ == '__main__':  # Script will automatically run the app, as long as this script is run directly
    app.run(debug=True)     # 