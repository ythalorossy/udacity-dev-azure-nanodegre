import os
from app import app


if __name__ == "__main__":
    print(' ----->>>> Flask Python Application running in development server')
    app.run(debug=True, host="0.0.0.0", port="8000")