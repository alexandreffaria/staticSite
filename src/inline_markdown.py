from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
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

def split_nodes_image(old_nodes):
    new_nodes = []
    splitted_nodes = ""
    remainingText = ""
    for node in old_nodes:
        
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        
        exctractedImages = extract_markdown_images(node.text)
        if len(exctractedImages) == 0:
            new_nodes.append(node)
            continue

        for image in exctractedImages: 
            splitted_nodes = node.text.split(f"![{image[0]}]({image[1]})", 1)
            if len(splitted_nodes) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if len(splitted_nodes) > 1 and splitted_nodes[1] is not None: 
                remainingText = splitted_nodes[1]
            new_nodes.append(TextNode(
                splitted_nodes[0], text_type_text
            ))
            new_nodes.append(TextNode(
                image[0], text_type_image, image[1]
            ))
            node.text = splitted_nodes[1]
        if remainingText:
            new_nodes.append(TextNode(
                remainingText, text_type_text
            ))      
    return new_nodes





def split_nodes_link(old_nodes):
    new_nodes = []
    splitted_nodes = ""
    remainingText = ""
    for node in old_nodes:
        
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        
        exctractedLinks = extract_markdown_links(node.text)
        if len(exctractedLinks) == 0:
            new_nodes.append(node)
            continue

        for link in exctractedLinks: 
            splitted_nodes = node.text.split(f"[{link[0]}]({link[1]})", 1)
            if len(splitted_nodes) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if len(splitted_nodes) > 1 and splitted_nodes[1] is not None: 
                remainingText = splitted_nodes[1]
            new_nodes.append(TextNode(
                splitted_nodes[0], text_type_text
            ))
            new_nodes.append(TextNode(
                link[0], text_type_link, link[1]
            ))
            node.text = splitted_nodes[1]
        if remainingText:
            new_nodes.append(TextNode(
                remainingText, text_type_text
            ))      
    return new_nodes

