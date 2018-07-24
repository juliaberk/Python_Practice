# Log rotate, but not!

# Let's say there are 9 files and we want to keep the most recent 5

import os
import argparse

#  Create a parser
parser = argparse.ArgumentParser(description='Time to rotate some log files!')
