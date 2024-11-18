import typing

import requests
from bs4 import BeautifulSoup, ResultSet, Tag

import src
import src.textParser


def main() -> None:
    data: dict[str, typing.List[str]] = {
        "journals_magazines": [],
        "proceedings_books": [],
    }

    authorID: str = "99660630871"
    # authorID: str = "fred"
    resp: requests.Response = src.download.getAuthorPublications(
        authorID=authorID,
    )

    if isinstance(resp, bool):
        raise Exception(
            f"Unable to connect to ACM DL with author ID {authorID}",
        )

    soup: BeautifulSoup = BeautifulSoup(markup=resp.content, features="lxml")

    journals: ResultSet[Tag] = src.htmlParser.readJournalMagazineNames(
        soup=soup,
    )

    journal: Tag
    for journal in journals:
        journalAcronymn: str = src.textParser.getAcronymn(text=journal.text)
        data["journals_magazines"].append(journalAcronymn)

    proceedings: ResultSet[Tag] = src.htmlParser.readProceedingsBookNames(
        soup=soup,
    )

    proceeding: Tag
    for proceeding in proceedings:
        proceedingAcronymn: str = src.textParser.getAcronymn(
            text=proceeding.text,
        )
        data["proceedings_books"].append(proceedingAcronymn)


if __name__ == "__main__":
    main()
