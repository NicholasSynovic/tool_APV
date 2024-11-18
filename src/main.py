import pathlib
import typing

import click
import pandas
import requests
from bs4 import BeautifulSoup, ResultSet, Tag

import src
import src.download
import src.htmlParser
import src.textParser


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
    help="Output CSV path",
    default=pathlib.Path("./output.csv"),
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
    data: dict[str, typing.List[str]] = {
        "journals_magazines": [],
        "proceedings_books": [],
    }

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

    df: pandas.DataFrame = pandas.DataFrame(data=data)
    df.to_csv(path_or_buf=outputPath)


if __name__ == "__main__":
    main()
