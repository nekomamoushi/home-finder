
import argparse
import logging
from logger import setup_logging

setup_logging(__name__)
logger = logging.getLogger(__name__)

def cli():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='help', help="Show help message and exit.")
    args = parser.parse_args()


if __name__ == "__main__":
    cli()
