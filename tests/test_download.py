import typing

import requests

import src
import src.download


def test_getAuthorPublications() -> None:
    VALID_AUTHOR_ID: str = "99660630871"  # Nicholas M. Synovic ID
    INVALID_AUTHOR_ID: str = "fred"

    resp: requests.Response = src.download.getAuthorPublications(
        authorID=VALID_AUTHOR_ID,
    )

    assert isinstance(resp, requests.Response)
    assert resp.status_code == 200

    resp: typing.Literal[False] = src.download.getAuthorPublications(
        authorID=INVALID_AUTHOR_ID,
    )

    assert isinstance(resp, bool)
    assert resp is False
