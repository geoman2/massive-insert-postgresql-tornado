"""Configuration file
"""
import os

TORNADO_PORT = os.environ.get("TORNADO_PORT")
assert TORNADO_PORT is not None

DB_NAME = os.environ.get("DB_NAME")
assert DB_NAME is not None

DB_USER = os.environ.get("DB_USER")
assert DB_USER is not None

DB_PASSWORD = os.environ.get("DB_PASSWORD")
assert DB_PASSWORD is not None

DB_HOST = os.environ.get("DB_HOST")
assert DB_HOST is not None
