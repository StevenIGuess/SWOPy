from datetime import datetime
import sys

def crashreport(msg):
    with open("../crshrprt.txt", "a") as crshrprt:
            crshrprt.write(f"{datetime.now()}::ERR::{msg}\n")
    sys.stderr.write(f"{datetime.now()}::ERR::{msg}")
    sys.exit(-1)