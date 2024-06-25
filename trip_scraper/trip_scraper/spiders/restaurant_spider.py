import scrapy

API_KEY = '5116d8272d3452283b011e9b4c578bf5'


class RestaurantItem:
    def __init__(self, url, rating, price_range, cuisine, meals, location, google_maps_link, website, email, phone_number):
        self.url = url
        self.rating = rating
        self.price_range = price_range
        self.cuisine = cuisine
        self.meals = meals
        self.location = location
        self.google_maps_link = google_maps_link
        self.website = website
        self.email = email
        self.phone_number = phone_number

    def to_dict(self):
        return {
            'url': self.url,
            'rating': self.rating,
            'price_range': self.price_range,
            'cuisine': self.cuisine,
            'meals': self.meals,
            'location': self.location,
            'google_maps_link': self.google_maps_link,
            'website': self.website,
            'email': self.email,
            'phone_number': self.phone_number
        }


class RestaurantSpider(scrapy.Spider):
    name = "restaurant_spider"
    start_urls = [
            'https://www.tripadvisor.com/Restaurants-g28926-California.html'
    ]
    
    def start_requests(self):
        yield scrapy.Request (
            url=self.start_urls[0], 
            callback=self.parse,
            meta={"proxy": "http://scraperapi:5116d8272d3452283b011e9b4c578bf5@proxy-server.scraperapi.com:8001"}
        )

    def parse(self, response):
        # Start by scraping city links from the first page and subsequent pages.
        yield from self.scrape_cities(response)

        # Continue by generating requests for pages 2 and 3.
        for page in range(2, 4):
            offset = (page - 1) * 20
            next_page_url = f'https://www.tripadvisor.com/Restaurants-g28926-oa{offset}-California.html'
            yield scrapy.Request(
                url=next_page_url, 
                callback=self.scrape_cities,
                meta={"proxy": "http://scraperapi:5116d8272d3452283b011e9b4c578bf5@proxy-server.scraperapi.com:8001"}
            )
        
    def scrape_cities(self, response):
        # if page 1
        if response.url == self.start_urls[0]:
            geo_name_links = response.css('div.geo_name a::attr(href)').getall()
            for city_link in geo_name_links:
                city_url = response.urljoin(city_link)
                yield {'city_url': city_url}
                
                # request to scrape restaurants
                yield scrapy.Request(
                    url=city_url, 
                    callback=self.scrape_restaurants,
                    meta={"proxy": "http://scraperapi:5116d8272d3452283b011e9b4c578bf5@proxy-server.scraperapi.com:8001"}
                )
        else:
            # Scraping subsequent pages: Extract city links from the list in subsequent pages
            li_elements = response.css('ul.geoList li')
            for li in li_elements:
                city_link = li.css('a::attr(href)').get()
                
                if city_link:
                    city_url = response.urljoin(city_link)
                    yield {'city_url': city_url}
                    
                    yield scrapy.Request(
                        url=city_url, 
                        callback=self.scrape_restaurants,
                        meta={"proxy": "http://scraperapi:5116d8272d3452283b011e9b4c578bf5@proxy-server.scraperapi.com:8001"}
                    )
            
    def scrape_restaurants(self, response):
        restaurant_links_divs = response.css('div.biGQs._P.fiohW.alXOW.NwcxK.GzNcM.ytVPx.UTQMg.RnEEZ.ngXxk')
        
        for div in restaurant_links_divs:
            a_tag = div.css('a.BMQDV._F.Gv.wSSLS.SwZTJ.FGwzt.ukgoS::attr(href)').get()
            if a_tag:
                restaurant_url = response.urljoin(a_tag)
                yield {'restaurant_url': restaurant_url}
                yield scrapy.Request(
                    url=restaurant_url, 
                    callback=self.scrape_restaurant_details,
                    meta={"proxy": "http://scraperapi:5116d8272d3452283b011e9b4c578bf5@proxy-server.scraperapi.com:8001"}
                )
                
    def scrape_restaurant_details(self, response):
        print("ONTO RESTAURANT DETAILS")
        rating = self.extract_rating(response)
        price_range, cuisine, meals = self.extract_details(response)
        location, google_maps_link = self.extract_location(response)
        website = self.extract_website(response)
        email = self.extract_email(response)
        phone_number = self.extract_phone_number(response)

        restaurant_item = RestaurantItem(
            response.url, rating, price_range, cuisine, meals, location, google_maps_link, website, email, phone_number
        )

        yield restaurant_item.to_dict()
        
        
    def extract_rating(self, response):
        rating_div = response.css('div.sOyfn.u.f.K')
        if rating_div:
            rating = rating_div.css('span.biGQs._P.fiohW.uuBRH::text').get().strip()
            return rating
        return "N/A"


    def extract_details(self, response):
        detail_divs = response.css('div.biGQs._P.pZUbB.alXOW.oCpZu.GzNcM.nvOhm.UTQMg.ZTpaU.W.hmDzD')
        if len(detail_divs) > 2:
            price_range = detail_divs[0].css('::text').get().strip()
            cuisine = detail_divs[1].css('::text').get().strip()
            meals = detail_divs[2].css('::text').get().strip()
            return price_range, cuisine, meals
        return "N/A", "N/A", "N/A"

    def extract_location(self, response):
        location_div = response.css('div.hpxwy.e.j')
        if location_div:
            location_link = location_div.css('a.BMQDV._F.Gv.wSSLS.SwZTJ.FGwzt.ukgoS')
            if location_link:
                google_maps_link = location_link.css('::attr(href)').get()
                location_span = location_link.css('span.biGQs._P.pZUbB.hmDzD::text').get()
                if location_span:
                    location = location_span.strip()
                    return location, google_maps_link
        return "N/A", "N/A"

    def extract_website(self, response):
        website_link = response.css('a[href^="http"]::attr(href)').get()
        if website_link:
            return website_link.strip()
        return "N/A"

    def extract_email(self, response):
        email_link = response.css('a[href^="mailto:"]::attr(href)').get()
        if email_link:
            return email_link.replace('mailto:', '').strip()
        return "N/A"

    def extract_phone_number(self, response):
        phone_link = response.css('a[href^="tel:"]::attr(href)').get()
        if phone_link:
            return phone_link.replace('tel:', '').strip()
        return "N/A"