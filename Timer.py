#!/usr/bin/env python3
import time

start_time = time.time()

try:
    while True:
        current_time = time.time() - start_time
        minutes, seconds = divmod(int(current_time), 60)
        print(f"\r{minutes:02d}:{seconds:02d}", end="")
        time.sleep(1)

except KeyboardInterrupt:
    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    print(f"\nElapsed time: {minutes:02d}:{seconds:02d}")
