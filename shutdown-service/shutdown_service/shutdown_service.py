import logging
import time
import signal
import threading
from shutdown_service.config import ShutdownServiceConfig

logger = logging.getLogger(__name__)

def run_stage():

    stop_event = threading.Event()

    # Register signal handlers
    def sig_handler(signum, _):
        signame = signal.Signals(signum).name
        print(f'Caught signal {signame} ({signum}). Exiting...')
        stop_event.set()

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    CONFIG = ShutdownServiceConfig()
    logging.basicConfig(level=CONFIG.log_level.value, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.setLevel(CONFIG.log_level.value)

    while True:
        logger.info("Shutdown service is running...")
        time.sleep(1)
        if stop_event.is_set():
            break