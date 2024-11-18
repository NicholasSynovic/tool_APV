import re

NO_PARENTHESIS_REGEX: str = r"^.*?(?=\s*\()"


def getAcronymn(text: str) -> str:
    text = text.strip()
    text = re.match(pattern=NO_PARENTHESIS_REGEX, string=text)[0]
    text = text.split(sep=":")[0]
    text = text.split(sep=" ")[0]
    return text
