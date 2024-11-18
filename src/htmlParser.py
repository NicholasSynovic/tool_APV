from bs4 import BeautifulSoup, ResultSet, Tag


def _readDiv(soup: BeautifulSoup, divID: str) -> ResultSet[Tag]:
    div: Tag = soup.find(
        name="div",
        attrs={"id": divID},
    )
    return div.find_all(name="span", attrs={"class": "facet__label"})


def readJournalMagazineNames(soup: BeautifulSoup) -> ResultSet[Tag]:
    return _readDiv(soup=soup, divID="Journal/MagazineNames")


def readProceedingsBookNames(soup: BeautifulSoup) -> ResultSet[Tag]:
    return _readDiv(soup=soup, divID="Proceedings/BookNames")
