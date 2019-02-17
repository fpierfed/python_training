#!/usr/bin/env python3
from datetime import datetime
import shutil
import sys
import time


w, _ = shutil.get_terminal_size()
t0 = datetime.now()
try:
    while True:
        s, ms = str(datetime.now() - t0).rsplit('.', 1)
        s = f'{s}.{ms[0]}'
        print(f'{s:>{w}}', end='\r', file=sys.stdout)
        sys.stdout.flush()
        time.sleep(.1)
except KeyboardInterrupt:
    sys.exit(0)
