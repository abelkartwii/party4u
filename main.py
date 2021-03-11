import spotipy
import pandas
import psycopg2
import sys
from spotipy import Spotify
from database import Database

def main():
    db = Database()