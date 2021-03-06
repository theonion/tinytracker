import base64
import collections
import os
import sys
import time
import urlparse

import gevent
from gevent import queue
from gevent import socket

event_queue = queue.Queue()
CARBON_ENDPOINT = os.environ.get("CARBON_ENDPOINT")
INTERVAL = int(os.environ.get("INTERVAL", "10"))
GIF_DATA = base64.b64decode("R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==")


def send_events(message):
    if CARBON_ENDPOINT:
        sock = socket.create_connection((CARBON_ENDPOINT.split(":")))
        sock.sendall(message)
        sock.close()
    else:
        print(message)


def count_events():
    
    while True:
        gevent.sleep(INTERVAL)
        counter = collections.Counter()

        now = int(time.time())

        while True:
            try:
                event = event_queue.get_nowait()
            except queue.Empty:
                break
            counter[event] += 1

        if len(counter):
            lines = []

            for key, value in counter.items():
                lines.append("tinytracker.{} {} {}".format(key, value, now))
            
            message = "\n".join(lines) + "\n"
            gevent.spawn(send_events, message)
gevent.spawn(count_events)


def application(env, start_response):
    if env["PATH_INFO"] == "/track.gif":
        start_response("200 OK", [("Content-Type", "image/gif")])
        yield GIF_DATA

        parsed = urlparse.parse_qs(env["QUERY_STRING"])

        events = parsed.get("event", [])
        for event in events:
            event_queue.put(event)
    else:
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        yield "Nothing here."
