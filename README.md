    # Python Scraper for PokeAPI

    ## Application

    At startup time a function runs to crawl the PokeAPI, and store all Pokemons in a SQLlite DB.
    This process takes around 30 seconds, and afterwards the DB is ready to receive requests to the
    Pokemon Display API. (Example in last section)

    In the main.py there are the definitions of the APIs, and also the startup functions.
    Inside the app folder, there's the schema definition in database.py, crawling functions in crawler.py and the service to run the `/pokemon/{name}` API.

    The schema of the DB is very simple. I simply stored the name, height, abilities and stats of each Pokemon. Since we are only storing Pokemons and their attributes, did not make sense to create a complicated schema.

    Regarding scaling the application, I would focus on: adding multiprocessing capabilities to the crawler, so that the DB setup is faster.

    I only added tests to the pokemon.py functionality, but the rest of the code would also be tested in the same way.


    There's a small script to lint the codebase (`./lint.sh`).

    ## Running the app: 

    Python 3.8+ required

    `pip install -r requirements`

    `uvicorn main:app`

    Using Docker: 
    ```
    docker build --tag cybsafe .
    docker run cybsafe
    ```


    ## Example request to the `/pokemon/{name}` API:

    ```
    curl -X 'GET' \
    'http://127.0.0.1:8000/pokemon/pikachu' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{}'
    ```

    Run tests: `pytest app`