import os
import logging
from robyn import Robyn

# Create the Robyn app instance
app = Robyn(__file__)

from app.routes.auth import setup_auth_routes

# Set up logging configuration
# Get a logger instance for the current module
logger = logging.getLogger(__name__)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/health")
async def health():
    return {"status": "ok"}

@app.startup_handler
def main() -> None:
    logger.info("Finished startup_handler")

@app.shutdown_handler
async def shutdown_handler() -> None:
    logger.info("Shutting down...")

if __name__ == "__main__":
    setup_auth_routes(app)
    app_port = int(os.environ.get("ROBYN_PORT", 9000))
    logger.info("Starting the application")
    app.start(host="0.0.0.0", port=app_port)