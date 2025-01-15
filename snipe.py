import httpx
import argparse
import asyncio

import base64

from OpenSSL import crypto

from datetime import datetime


seprator = "=" * 80


class ApiEndpoints:
    def __init__(self, owner: str, repo: str, token: str):
        self.github_host: str = "https://api.github.com"
        self.owner = owner
        self.repo = repo
        self.headers: dict = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
        }

    def get_repository_content(self):
        return {
            "url": f"{self.github_host}/repos/{self.owner}/{self.repo}/contents",
            "headers": self.headers,
        }


def argument_parser():
    _arg_parse = argparse.ArgumentParser(prog="sniper snipe file pattern")
    _arg_parse.add_argument(
        "--token", required=True, help="authentication token", metavar="", type=str
    )
    _arg_parse.add_argument(
        "--owner", required=True, help="github project owner", metavar="", type=str
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


async def get_files(url: str, headers: dict, path: str = "") -> list:
    async with httpx.AsyncClient() as client:
        response = await client.get(url=f"{url}/{path}", headers=headers)
        response.raise_for_status()
        contents = response.json()

    files = []

    for item in contents:
        if item["type"] == "file":
            files.append(item["path"])
        elif item["type"] == "dir":
            nested_files = await get_files(url, headers, item["path"])
            files += nested_files

    return files


def get_file_content(url: str, headers: dict, paths: list):
    for item in paths:
        with httpx.Client() as client:
            response = client.get(url=f"{url}/{item}", headers=headers)
            response.raise_for_status
            contents = response.json()
            cert_data = base64.b64decode(contents["content"]).decode("utf-8")

        cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_data)

        expiry_date = cert.get_notAfter().decode("utf-8")
        expiry_date = datetime.strptime(expiry_date, "%Y%m%d%H%M%SZ")

        print(f"Certificate             : {item}")
        print(f"Certificate Content     : \n{cert_data}")
        print(f"Certificate Expiry Date : {expiry_date}")
        print(seprator)


def filter(files: list, patterns: tuple):
    filtered_files = []
    for item in files:
        if item.endswith(patterns):
            filtered_files.append(item)
    return filtered_files


def main():
    args = argument_parser()
    instance = ApiEndpoints(owner=args.owner, repo=args.repo, token=args.token)
    patterns = (
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

    # Get all files from a given repository
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


if __name__ == "__main__":
    main()
