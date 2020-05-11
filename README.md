## Tech journal spiders

Scraping articles about new technologies from [The Verge](https://www.theverge.com/tech "www.theverge.com") (Tech) and [Insight.com](https://www.insight.com/ "www.insight.com").

All data will be stored inside MongoDB.

### `scrapy crawl <spide_name>`

<spider_name> - Name of the spider to run

Available spiders:
1. insight
2. verge

### Setup process

1. Install `python 3.7+` and if you want to create a virtual environment - `pipenv --python 3.7`
2. Install [MongoDB](https://www.mongodb.com/ "MongoDB") to store the data
3. Run: `pip install` to get needed dependencies
4. Create `.env` file in the insight directory (next to the file `scrapy.cfg`) with the next data:

````
MONGODB_HOST = ''
DATABASE = 'journals'
COLLECTION = 'articles'
````

Where:

MONGODB_HOST - database address (`mongodb://localhost/<database>`)

DATABASE - database name

COLLECTION - collection name
