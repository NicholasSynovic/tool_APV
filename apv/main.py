import json
import pathlib
import typing

import click
import requests
from bs4 import BeautifulSoup, ResultSet, Tag

import apv


@click.command()
@click.option(
    "-a",
    "--author-id",
    "authorID",
    type=str,
    nargs=1,
    required=False,
    help="ACM DL author ID",
    default="99660630871",
    show_default=True,
)
@click.option(
    "-o",
    "--output",
    "outputPath",
    nargs=1,
    required=False,
    help="Output JSON path",
    default=pathlib.Path("./output.json"),
    show_default=True,
    type=click.Path(
        exists=False,
        file_okay=True,
        writable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
)
def main(authorID: str, outputPath: pathlib.Path) -> None:
    """
    A utility to get ACM Author publication venues.

    An Exception is thrown if the author ID is invalid.
    """
    data: dict[str, typing.List[str]] = {
        "journals_magazines": [],
        "proceedings_books": [],
    }

    resp: requests.Response = apv.getAuthorPublications(
        authorID=authorID,
    )

    if isinstance(resp, bool):
        raise Exception(
            f"Unable to connect to ACM DL with author ID {authorID}",
        )

    soup: BeautifulSoup = BeautifulSoup(markup=resp.content, features="lxml")

    journals: ResultSet[Tag] = apv.readJournalMagazineNames(
        soup=soup,
    )

    journal: Tag
    for journal in journals:
        if journal.text is None:
            continue

        data["journals_magazines"].append(journal.text)

    proceedings: ResultSet[Tag] = apv.readProceedingsBookNames(
        soup=soup,
    )

    proceeding: Tag
    for proceeding in proceedings:
        data["proceedings_books"].append(proceeding.text)

    json.dump(obj=data, fp=open(file=outputPath, mode="w"), indent=4)


if __name__ == "__main__":
    main()
