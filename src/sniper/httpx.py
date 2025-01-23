# -*- coding: utf-8 -*-

import httpx
import base64
from OpenSSL import crypto
from datetime import datetime


seprator = "=" * 80


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
