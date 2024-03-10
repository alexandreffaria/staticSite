from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        split_nodes = []
        splited = node.text.split(delimiter)
        if len(splited) % 2 == 0:
            raise Exception(f"Markdown syntax error: missing closing {delimiter}")

        for i in range(len(splited)):
            if splited[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(splited[i], text_type_text))
            else:
                split_nodes.append(TextNode(splited[i], text_type))

        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    match = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    if len(match) == 0:
        raise Exception("Could not find markdown for image")
    return match

def extract_markdown_links(text):
    match = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    if len(match) == 0:
        raise Exception("Could not find markdown for link")
    return match