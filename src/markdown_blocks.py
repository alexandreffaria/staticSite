block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

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
            return block_type_unordered_list
    elif markdown[0] == "1" and markdown[1] == ".":
        countLinesList = 0
        for i, line in enumerate(markdown.split("\n")):
            if int(line[0]) == i+1:
                countLinesList += 1
        if countLinesList == len(markdown.split("\n")):
            return block_type_ordered_list
    else: 
        return block_type_paragraph