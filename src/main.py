import requests
from bs4 import BeautifulSoup, ResultSet, Tag

import src
import src.download
import src.htmlParser


def main() -> None:
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

    # journals: ResultSet[Tag] = src.htmlParser.readJournalMagazineNames(
    #     soup=soup,
    # )

    proceedings: ResultSet[Tag] = src.htmlParser.readProceedingsBookNames(
        soup=soup,
    )

    for proceeding in proceedings:
        print(proceeding.text)


if __name__ == "__main__":
    main()
