# -*- coding: utf-8 -*-


def filter(files: list, patterns: tuple):
    filtered_files = []
    for item in files:
        if item.endswith(patterns):
            filtered_files.append(item)
    return filtered_files
