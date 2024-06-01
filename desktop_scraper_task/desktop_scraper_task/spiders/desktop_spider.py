import scrapy

class DesktopSpider(scrapy.Spider):
    name = "get_computers_data"
    start_urls = ["https://desktop.bg/computers-all"]

    def parse(self, response):
        products = response.css("ul.products > li")

        for product in products:
            if "ad" in product.attrib.get("class", ""):
                continue

            product_page_url = product.css("a::attr(href), article > a::attr(href)").get()

            if product_page_url:
                yield response.follow(product_page_url, self.parse_product_details)

        # Follow pagination links
        next_page = response.css('li.next-page > a').attrib['href'] + "https:/"
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        
    def parse_product_details(self, response):

        cpu_name_element = response.css('div.frame>header>h1::text').get()
        processor_element = response.xpath('//tr[th[contains(text(), "Процесор")]]/td').get()
        motherboard_element = response.xpath('//tr[th[contains(text(), "Дънна платка")]]/td').get()
        gpu_element = response.xpath('//tr[th[contains(text(), "Видеокарта")]]/td').get()

        if not (cpu_name_element and processor_element and motherboard_element and gpu_element):
            self.logger.info(f"Skipped non-product page: {response.url}")
            return

        try:
            cpu_name = cpu_name_element.strip()
            
            # Processor extraction
            processor_name = response.xpath('//tr[th[contains(text(), "Процесор")]]/td//div[@class="default-option options"]/label/span/text()').get()
            if not processor_name:
                processor_name = response.xpath('//tr[th[contains(text(), "Процесор")]]/td/text()').get()
            processor_name = processor_name.strip() 

            # Motherboard extraction
            motherboard_name = response.xpath('//tr[th[contains(text(), "Дънна платка")]]/td//div[@class="default-option options"]/label/span/text()').get()
            if not motherboard_name:
                motherboard_name = response.xpath('//tr[th[contains(text(), "Дънна платка")]]/td/text()').get()
            motherboard_name = motherboard_name.strip() 

            # GPU extraction
            gpu_name = response.xpath('//tr[th[contains(text(), "Видеокарта")]]/td//div[@class="default-option options"]/label/span/text()').get()
            if not gpu_name:
                gpu_name = response.xpath('//tr[th[contains(text(), "Видеокарта")]]/td/text()').get()
            gpu_name = gpu_name.strip()
            
            # RAM extraction
            ram_name = response.css('tr.DesktopRam.default-option.options span::text').get()
            if not ram_name:
                ram_name = response.xpath('//tr[th[contains(text(), "Оперативна памет")]]/td//div[@class="default-option options"]/label/span/text()').get()
            if not ram_name:
                ram_name = response.xpath('//tr[th[contains(text(), "Оперативна памет")]]/td/text()').get()
            ram = ram_name.strip() 
  
            yield {
                "cpu_name": cpu_name,
                "processor": processor_name,
                "motherboard": motherboard_name,
                "gpu": gpu_name,
                "ram": ram,
            }
        except AttributeError:
            self.logger.error(f"Missing data in product: {response.url}")

