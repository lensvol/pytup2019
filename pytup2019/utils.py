import re

CORRECTIONS = {
    re.compile(r"\b{0}\b".format(pattern), re.IGNORECASE): replacement
    for pattern, replacement in (("json", "JSON"), ("yaml", "YAML"))
}


def fix_spelling(text):
    for pattern, replacement in CORRECTIONS.items():
        text = re.sub(pattern, replacement, text)

    return text
