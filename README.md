# Docker for Mac download links

Inspired by [docker/for-mac#1120](https://github.com/docker/for-mac/issues/1120).

## Usage

Install the python dependencies:

```
virtualenv -p python3 venv
./venv/bin/pip install -r requirements.txt
```

And execute the scraper:

```
> ./venv/bin/python3 script.py --help
usage: scrape.py [-h] [--limit LIMIT] [--out OUT] {stable,edge}

Scrape for Docker for Mac release download links

positional arguments:
  {stable,edge}

optional arguments:
  -h, --help     show this help message and exit
  --limit LIMIT  Maximum number of builds to scan for
  --out OUT      JSON file to output build info
```

## Example

Scrape for the latest 1000 builds of the stable channel:

```
> ./venv/bin/python3 script.py stable --out stable.json --limit=1000
```
