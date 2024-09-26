"""This module provides the command line argument parser.

The command line argument parser is used to parse the command line arguments
when starting the hackaton bot.

Functions
---------
get_args
    Parses the command line arguments.

Classes
-------
Arguments
    Represents the parsed arguments from the command line.
"""

import argparse
import sys
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Arguments:
    """Represents the parsed arguments from the command line.

    Attributes
    ----------
    host: :class:`str`
        The host address.
    port: :class:`int`
        The port to connect to.
    code: :class:`str`
        The optional game code for joining specific lobby.
    nickname: :class:`str`
        The player's nickname.
    """

    host: str
    port: int
    code: Optional[str]
    nickname: str


def get_args() -> Arguments:
    """Parses the command line arguments.

    Returns
    -------
    Arguments
        The parsed arguments from the command line.
    """

    parser = argparse.ArgumentParser(description="Game Client Argument Parser")

    parser.add_argument(
        "--host",
        type=str,
        default="localhost",
        help="Host address (default: localhost)",
    )

    parser.add_argument(
        "--port", type=int, default=5000, help="Port to connect to (default: 5000)"
    )

    parser.add_argument(
        "--code",
        type=str,
        default=None,
        help="Optional game code for joining specific lobby",
    )

    parser.add_argument(
        "--nickname", type=str, required=True, help="Player's nickname (required)"
    )

    try:
        args = parser.parse_args()
    except SystemExit:
        parser.print_help()
        sys.exit(1)

    return Arguments(
        host=args.host,
        port=args.port,
        code=args.code,
        nickname=args.nickname,
    )