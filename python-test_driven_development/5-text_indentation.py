#!/usr/bin/python3
"""text_indentation"""


def text_indentation(text):
    """text_indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ['.', '?', ':']:
            result += "\n\n"
    lines = result.splitlines()
    stripped_lines = [line.strip() for line in lines]
    final_text = "\n".join(stripped_lines)
    print(final_text)
