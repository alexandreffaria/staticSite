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

