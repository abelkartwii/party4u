import psycopg2
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read_file(open(f"{Path(__file__).parents[0]}/config.cfg"))

class Database:
    def __init__(self):
        # connects to postgres with the details in config.cfg
        self._conn = psycopg2.connect("host = {} dbname = {} user = {} password = {} port = {}".format(*config['DATABASE'].values()))
        self._cur = self._conn.cursor()

    def execute(self, query):
        # executes the queries passed in main.py
        self._cur.execute(query)

    def setup(self):
        # sets up the schema and table if they don't exist yet
        self.execute(create_lastfm_schema)
        self.execute(create_lastfm_table)