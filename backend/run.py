# run.py

from app import create_app, config_class

app = create_app(config_class)

if __name__ == "__main__":
    app.run()
