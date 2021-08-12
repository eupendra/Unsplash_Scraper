from unsplash.spiders.unsplash_spider import UnsplashSpider
from argparse import ArgumentParser
import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def run_spider(search_term, max_pages):
    start_time = time.time()
    settings = get_project_settings()
    settings['LOG_LEVEL'] = 'WARN'
    settings['AUTOTHROTTLE_ENABLED'] = True
    process = CrawlerProcess(settings)
    process.crawl(UnsplashSpider, search_term=search_term, max_pages=max_pages)
    process.start()
    print("\n\n{:.2f} Seconds".format(time.time() - start_time))
    

def main():
    parser= ArgumentParser(description="Unsplash Scraper")
    # parser.print_help("this is help")
    parser.add_argument("-s", "--search", 
                        help="Search Term", 
                        required=True)
    parser.add_argument("-p", "--pages", 
                        help="Numper of Pages to Scrape", 
                        required=False,
                        default=1)
    
    args = parser.parse_args()
    run_spider(args.search, args.pages)
    
    
if __name__ == "__main__":
    main()
    