from bs4 import BeautifulSoup, ResultSet, Tag


def _readDiv(soup: BeautifulSoup, divID: str) -> ResultSet[Tag]:
    """
    Given an HTML div tag, return a set of all the span tags underneath it

    :param soup: BeuatifulSoup HTML object
    :type soup: BeautifulSoup
    :param divID: The id attribute of a div object
    :type divID: str
    :return: A set of all span tags that are children of the div tag
    :rtype: ResultSet[Tag]
    """
    div: Tag = soup.find(
        name="div",
        attrs={"id": divID},
    )
    return div.find_all(name="span", attrs={"class": "facet__label"})


def readJournalMagazineNames(soup: BeautifulSoup) -> ResultSet[Tag]:
    """
    Return the list of journal and magazine names that an author has published in

    :param soup: BeuatifulSoup HTML object
    :type soup: BeautifulSoup
    :return: The set of all journal and magazine span tags
    :rtype: ResultSet[Tag]
    """  # noqa: E501
    return _readDiv(soup=soup, divID="Journal/MagazineNames")


def readProceedingsBookNames(soup: BeautifulSoup) -> ResultSet[Tag]:
    """
    Return the list of proceeding and book names that an author has published in

    :param soup: BeuatifulSoup HTML object
    :type soup: BeautifulSoup
    :return: The set of all proceeding and book span tags
    :rtype: ResultSet[Tag]
    """  # noqa: E501
    return _readDiv(soup=soup, divID="Proceedings/BookNames")
