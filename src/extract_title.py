def extract_title(markdown):
    lines = markdown.split("\n")
    h1 = None
    for line in lines:
        if line.startswith("#"):
            checkH1 = line.split(" ")[0]
            if len(checkH1) < 2:
                h1 = line
    if h1:
        return h1
    else:
        raise ValueError("Every page should have a h1")
