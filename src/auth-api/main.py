"""
    Auth API launcher.
"""

# Server.
import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", port=80)