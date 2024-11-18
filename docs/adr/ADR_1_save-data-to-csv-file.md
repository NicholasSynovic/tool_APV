# 1. Save data to CSV file

## Context

After we have extracted the data from the ACM DL HTML content, we need to save
the data to disk somewhere.

CSV is a lightweight, widely accepted, and easily importable format to write
data to for further analytics.

## Decision

Using `pandas`, convert the data into a `pandas.DataFrame` and then write it to
disk.

## Consequences

We will have to add `pandas` as a dependency.

Additionally, we will need to have a command line option to specify a storage
location.
