import logging
from app import create_app

app = create_app()

# Configure Flask's logger to handle higher-level logs
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    app.run(debug=True)
