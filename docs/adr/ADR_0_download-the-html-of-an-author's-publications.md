# 0. Download the HTML of an author's publications

## Context

We need to get a list of publications that an author has published.

Thus, given an ACM DL author ID, get the list of publications in HTML format.

## Decision

We will use the `request` library to make the `HTTP GET` call.

The HTML content will be stored in memory rather than on disk.

## Consequences

Once we have the `HTML` content, we will need to use `BeautifulSoup` to parse
the file and get information out.

However, as the `HTML` content of the site will change over time, the `HTML`
parser will need to be updated to match that.
