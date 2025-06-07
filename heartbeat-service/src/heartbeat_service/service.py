#!/usr/bin/env python

import time
import typer
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("heartbeat-service")

def heartbeat(interval: int = 5):
    """
    Run a heartbeat service that logs a message every specified interval.
    
    Args:
        interval: Time between heartbeats in seconds
    """
    logger.info(f"Starting heartbeat service with {interval} second interval")
    try:
        while True:
            logger.info(f"Heartbeat at {datetime.now().isoformat()}")
            time.sleep(interval)
    except KeyboardInterrupt:
        logger.info("Heartbeat service stopped")

def main():
    typer.run(heartbeat)

if __name__ == "__main__":
    main()
