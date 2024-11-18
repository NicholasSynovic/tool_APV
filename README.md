# Author Publication Venues

> A utility to get ACM Author publication venues

## Table of Contents

- [Author Publication Venues](#author-publication-venues)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How To Install](#how-to-install)
  - [How To Run](#how-to-run)
  - [Documentation](#documentation)
    - [JSON Schema](#json-schema)

## About

`apv` gets the publication venues of where an ACM author has published from
their public ACM DL publications page.

I wrote this utility in order to help Ph.D. students identify which venue(s)
their mentors, advisors, and colleagues publish in (so long as their tracked by
ACM). The goal for this is not to track publications per say, but to identify
the set of venues that a user may want to read more about or submit a manuscript
to.

## How To Install

Assuming that you have `git clone`d the repository:

1. `make create-dev`
1. `source env/bin/activate`
1. `make build`

## How To Run

`apv --help`

```shell
Usage: apv [OPTIONS]

  A utility to get ACM Author publication venues.

  An Exception is thrown if the author ID is invalid.

Options:
  -a, --author-id TEXT  ACM DL author ID  [default: 99660630871]
  -o, --output PATH     Output JSON path  [default: output.json]
  --help                Show this message and exit.
```

**NOTE**: by default, my (Nicholas M. Synovic's) ACM DL author ID is used

## Documentation

API docs are provided for the project within the source files.

### JSON Schema

The output JSON data follows this schema:

```json
{
    "$schema": "http://json-schema.org/draft-06/schema#",
    "$ref": "#/definitions/Apv",
    "definitions": {
        "APV": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "journals_magazines": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "proceedings_books": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": [
                "journals_magazines",
                "proceedings_books"
            ],
            "title": "APV"
        }
    }
}
```
