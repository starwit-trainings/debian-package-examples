"""Command line interface for Heartbeat App."""

import logging
from .config import ApplicationConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("heartbeat-app")

def main():
    """Run the main application."""
    logger.info("Hello from heartbeat app!")
    config = ApplicationConfig()
    logger.info("Config: %s", config)


if __name__ == "__main__":
    main()