import string
import typing

import requests

AUTHOR_URL_TEMPLATE: string.Template = string.Template(
    template="https://dl.acm.org/profile/${AUTHOR_ID}/publications?Role=author",  # noqa: E501
)


def getAuthorPublications(
    authorID: str,
) -> requests.Response | typing.Literal[False]:  # noqa: E501
    authorURL: str = AUTHOR_URL_TEMPLATE.substitute(AUTHOR_ID=authorID)
    resp: requests.Response = requests.get(url=authorURL, timeout=60)

    if resp.status_code == 200:
        return resp
    else:
        return False
