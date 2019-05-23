
import argparse
import logging

from home_finder.utils.log import setup_logging, setup_logging_dependencies
from home_finder.core import check_settings, execute

logger = logging.getLogger(__name__)


def check_args():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '-h', '--help',
        action='help',
        help="Show help message and exit."
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        dest='debug',
        default=False
    )
    args = parser.parse_args()
    return args


def configure_logging(debug):
    log_level = logging.DEBUG if debug else logging.INFO
    setup_logging(log_level)
    setup_logging_dependencies()


def cli():
    args = check_args()
    configure_logging(args.debug)
    settings = check_settings()
    execute(settings)


if __name__ == "__main__":
    cli()
