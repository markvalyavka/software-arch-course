from facade_service.app import init_app
import time

app = init_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

