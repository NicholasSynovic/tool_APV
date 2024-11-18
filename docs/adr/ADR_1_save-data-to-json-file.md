# 1. Save data to JSON file

## Context

After we have extracted the data from the ACM DL HTML content, we need to save
the data to disk somewhere.

JSON is a lightweight, widely accepted, and easily importable format to write
data to for further analytics.

## Decision

Using `json`, convert the data into a JSON file and then write it to disk.

## Consequences

We will need to have a command line option to specify a storage location.
