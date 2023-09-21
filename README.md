# CryptoReport Scrapy Project
This is a web scraping project to fetch the latest posts from Cointelegraph and compile them into a JSON file.

1.0 - Initial Config

## Setup and Execution

#### 1. Install, Create and Activate a Virtual Environment

If you haven't installed Conda yet, [download it here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) and follow the installation instructions for your operating system.

Once Conda is installed, you can create a virtual environment. This will keep the project's dependencies isolated from global packages and other projects.

`conda create --name cryptoreport python=3.11.5`

And them, activate your venv

`conda activate cryptoreport` 

#### 3. Clone the Repository
Navigate to the directory where you'd like to keep the project and run:

`git clone https://github.com/uphiago/scrapycointelegraph`
 

#### 4. Install Required Packages
With the virtual environment activated, you can install the necessary Python packages from main directory using:

`pip install -r requirements.txt` 

#### 5. Run the Scrapy Spider

Navigate to the location of `cointelegraph.py`:

`cd scrapycointelegraph/cryptoreport/cryptoreport/spiders` 

Then, run the Scrapy spider with:

`scrapy crawl cointelegraph -O articles.json` 

This will save the scraped data into `articles.json`.
