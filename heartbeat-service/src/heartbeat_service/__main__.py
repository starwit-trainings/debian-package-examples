#!/usr/bin/env python
import signal
import sys

from heartbeat_service import heartbeat

def signal_handler(sig, frame):
    print('Got SIGINT - shutting down')
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    print('Starting service. Send  SIGINT to shutdown.')
    signal.pause()    
    heartbeat()