import psycopg2
import smtplib
import ssl
import json
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tabulate import tabulate

def mail4u():
    conn = psycopg2.connect(host = "", port = "", dbname = "")
    cursor = conn.cursor()

    # determine time window for one week
    today = datetime.today().date()
    last_week = today - timedelta(days = 7)


    ####
    top_five_songs = [["Song Name", "Minutes"]]
    cursor.callproc("spotify_schema.function_last_7_days_top_5_songs_duration")
    for row in cursor.fetchall():
        song_name = row[0]
        listened = float(row[1])
        element = [song_name, listened]
        top_five_songs.append(element)

    ####

    # sends email
    port = ""
    password = ""

    sender_email = ""
    receiver_email = ""

    text = f"""\
    Hi honey!
    Dates included: {last_week} - {today}:
    """