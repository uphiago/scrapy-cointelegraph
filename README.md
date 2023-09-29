# Cryptoreport Scrapy Project
This is a web scraping project to fetch the latest posts from Cointelegraph and compile them into a JSON file.


## Setup and Execution

#### 1. Install, Create and Activate a Virtual Environment

If you haven't installed Conda yet, [download it here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) and follow the installation instructions for your operating system.

Once Conda is installed, you can create a virtual environment. This will keep the project's dependencies isolated from global packages and other projects.

`conda create --name cryptoreport python=3.11.5`

And them, activate your venv

`conda activate cryptoreport` 

#### 2. Clone the Repository
Navigate to the directory where you'd like to keep the project and run:

`git clone https://github.com/uphiago/scrapycointelegraph`
 

#### 3. Install Required Packages
With the virtual environment activated, you can install the necessary Python packages from main directory using:

`pip install -r requirements.txt` 

#### 4. Set up and Launch Scrapy Splash
Scrapy Splash is used to render JavaScript on the pages we want to scrape. It uses a Docker image to do this.

4.1. First, ensure you have Docker installed on your machine. If not, [follow this guide](https://docs.docker.com/get-docker/) to get Docker up and running.

4.2. Once Docker is set up, pull the Scrapy Splash Docker image:
`sudo docker pull scrapinghub/splash`

4.3. After the image is pulled, run a Splash instance:
`sudo docker run -it -p 8050:8050 --rm scrapinghub/splash`

4.4. Confirm that Splash is running correctly by opening your web browser and navigating to:
`http://localhost:8050/`
You should see the Splash welcome page, indicating it's ready to be used by Scrapy.

#### 5. Run the Scrapy Spider

Navigate to the location of `cointelegraph.py`:

`cd scrapycointelegraph/cryptoreport/spiders` 

Then, run the Scrapy spider with:

`scrapy crawl cointelegraph -O articles.json` 

This will save the scraped data into `articles.json`.
