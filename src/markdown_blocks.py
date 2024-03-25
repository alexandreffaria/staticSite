from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n")
    groups = []
    groupingBlocks = ""
    for block in blocks:
        if block == "" and groupingBlocks:
            groups.append(groupingBlocks)
            groupingBlocks = ""
        else:
            if groupingBlocks:
                groupingBlocks += "\n" + block
            else:
                groupingBlocks += block
    if groupingBlocks:
        groups.append(groupingBlocks)
    return groups

def block_to_block_type(markdown):
    if (
        markdown.startswith("# ")
        or markdown.startswith("## ") 
        or markdown.startswith("### ") 
        or markdown.startswith("#### ") 
        or markdown.startswith("##### ") 
        or markdown.startswith("###### ") 
        ):
        return block_type_heading
    elif markdown.startswith("```") and markdown.endswith("```"):
        return block_type_code
    elif markdown.startswith(">"):
        codeLineCounter = 0
        for line in markdown.split("\n"):
            if line.startswith(">"):
                codeLineCounter += 1
        if len(markdown.split("\n")) == codeLineCounter:
            return block_type_quote
    elif markdown.startswith("*") or markdown.startswith("-"):
        codeLineCounter = 0
        for line in markdown.split("\n"):
            if line.startswith("*") or line.startswith("-"):
                codeLineCounter += 1
        if len(markdown.split("\n")) == codeLineCounter:
            return block_type_ulist
    elif markdown[0] == "1" and markdown[1] == ".":
        countLinesList = 0
        for i, line in enumerate(markdown.split("\n")):
            if int(line[0]) == i+1:
                countLinesList += 1
        if countLinesList == len(markdown.split("\n")):
            return block_type_olist
    else: 
        return block_type_paragraph

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")

def markdown_to_hmtl_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    hLevel = 0
    for char in block:
        if char == "#":
            hLevel += 1
        else:
            break

    if hLevel + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {hLevel}")
    text = block[hLevel + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{hLevel}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")

    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">") :
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)