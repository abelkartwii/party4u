# party4u
## Overview
This project leverages ETL in Python to retrieve the user's listening habits in Spotify and sends them a weekly roundup email of their statistics, automated using Apache Airflow.

Title taken from Charli XCX's [party4u](https://www.youtube.com/watch?v=fKrTCGGEiWY).

## Workflow
#### 1. Extract (Spotify Web API)
Data is extracted out of the Spotify API using Spotify's own HTTP endpoints, that can be found [here](https://developer.spotify.com/documentation/web-api/reference/). 

#### 2. Transform (pandas) // WIP
The Python `pandas` library is used to perform transformation on the data extracted from the Spotify API. The data is originally in the form of dictionaries, but through this step, the dictionaries will be transformed into pandas dataframes while some cleaning is performed on the values. This makes loading the data into PostgreSQL much more simpler!

#### 3. Load (PostgreSQL) // WIP
A local PostgreSQL database is created to store the transformed data.

#### Automation (Airflow)
Apache Airflow is used to create two DAGs: 
1. one to schedule the pipeline (`etl`),
2. one to schedule the weekly roundup email (`email`). 

## Configuration
Tools used in this project:
* [Python](https://www.python.org/downloads/) 3.9.2
* [Apache Airflow](https://spark.apache.org/downloads.html) 
* [Spotify Web API](https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-users-top-artists-and-tracks)

Required Python modules: `psycopg2`, `spotify`

To access Spotify data, first create a Spotify [developer account](https://developer.spotify.com/dashboard/login) here.

```
client_id = <insert client id here>
client_secret = <insert client secret here>
```

## License
This project uses the [MIT license](https://choosealicense.com/licenses/mit/).