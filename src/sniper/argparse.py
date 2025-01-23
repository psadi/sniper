# -*- coding: utf-8 -*-

import argparse


def argument_parser():
    _arg_parse = argparse.ArgumentParser(prog="sniper snipe file pattern")
    _arg_parse.add_argument(
        "--token", required=True, help="authentication token", metavar="", type=str
    )
    _arg_parse.add_argument(
        "--owner",
        "--org",
        required=True,
        help="github project owner/org",
        metavar="",
        type=str,
    )
    mg_1 = _arg_parse.add_mutually_exclusive_group()
    mg_1.add_argument("--repo", help="github repo name", metavar="", type=str)
    mg_1.add_argument(
        "--all",
        help="all repos for the given owner",
        metavar="",
        type=bool,
        default=True,
    )

    return _arg_parse.parse_args()
