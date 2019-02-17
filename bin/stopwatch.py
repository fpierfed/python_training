#!/usr/bin/env python3
import shutil
import sys
import time


w, _ = shutil.get_terminal_size()
t0 = time.time()
try:
    while True:
        print(f'{time.time() - t0:>{w}.01f}', end='\r', file=sys.stdout)
        sys.stdout.flush()
        time.sleep(.1)
except KeyboardInterrupt:
    sys.exit(0)
