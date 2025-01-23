# -*- coding: utf-8 -*-

from sniper.argparse import argument_parser
from sniper.api import ApiEndpoints
from sniper.httpx import get_file_content, get_files
from sniper.utils import filter
from typing import Union, Tuple

import asyncio


seprator = "=" * 80


def main() -> None:
    args = argument_parser()

    owner_or_org: str = args.owner if args.owner else args.org
    repo_or_all: Union[str, bool] = args.repo if args.repo else args.all

    instance: ApiEndpoints = ApiEndpoints(owner_or_org, repo_or_all, args.token)

    patterns: Tuple = (
        ".crt",
        ".pem",
        # ".der",
        # ".pfx",
        # ".p12",
        # ".cer",
        # ".key",
        # ".csr",
        # ".p7b",
        # ".p7c",
        # ".jks",
        # ".ssl",
        # ".spc",
    )

    payload = instance.get_repository_content()

    print(f"Sniping contents in '{args.owner}/{args.repo}' repository")
    print(seprator)
    files = asyncio.run(get_files(payload["url"], payload["headers"]))
    filtered_files = filter(files, patterns)

    print("\nFiles:\n")
    for index, item in enumerate(files, start=1):
        print(f"\t{index}: {item}")
    print(seprator)
    print("\nFiltered Files:\n")
    for index, item in enumerate(filtered_files, start=1):
        print(f"\t{index}: {item}")
    print(seprator)

    get_file_content(payload["url"], payload["headers"], filtered_files)
