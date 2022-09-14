from amazon_scraper import Scraper
from emailer import Emailer

urls = {
    "Sony WH-1000XM4": "https://www.amazon.com/Sony-WH-1000XM4-Canceling-Headphones-phone-call/dp/B0863TXGM3/ref=sr_1_1_sspa?crid=JB2HEKUD63R1&keywords=sony%2Bwh-1000xm4%2Bheadphones&qid=1663076613&s=electronics&sprefix=Sony%2BWH-1000XM4%2Celectronics%2C351&sr=1-1-spons&ufe=app_do%3Aamzn1.fos.ac2169a1-b668-44b9-8bd0-5ec63b24bcb5&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUzJUVEpSUjY2RUwxJmVuY3J5cHRlZElkPUEwNDE4NzI4MzNZTFdBVlpIUjBDRSZlbmNyeXB0ZWRBZElkPUEwOTgxNzIzMjJSQlU4NFROTjRKUiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1",
    "Sony WH-1000XM5": "https://www.amazon.com/Sony-WH-1000XM5-Canceling-Headphones-Hands-Free/dp/B09XS7JWHH/ref=sr_1_3?crid=3R6S0HH7OXAY&keywords=sony%2Bwh-1000xm5%2Bheadphones&qid=1663114485&s=electronics&sprefix=sony%2Bwh-1000xm5%2Bheadphones%2Celectronics%2C244&sr=1-3&ufe=app_do%3Aamzn1.fos.ac2169a1-b668-44b9-8bd0-5ec63b24bcb5",
    "Bose NCH 700": "https://www.amazon.com/Bose-Cancelling-Wireless-Bluetooth-Headphones/dp/B07Q9MJKBV/ref=sr_1_1_sspa?crid=3R6S0HH7OXAY&keywords=sony%2Bwh-1000xm5%2Bheadphones&qid=1663114518&s=electronics&sprefix=sony%2Bwh-1000xm5%2Bheadphones%2Celectronics%2C244&sr=1-1-spons&ufe=app_do%3Aamzn1.fos.ac2169a1-b668-44b9-8bd0-5ec63b24bcb5&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyT1FJNlRYRDJEM1o1JmVuY3J5cHRlZElkPUEwNTYyNTgyMTlQVVA1UjVQNUxaQiZlbmNyeXB0ZWRBZElkPUEwNDg5NjUyM0ZDOUpBUTFYQjE3SyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
}
backup_urls = {
    "Sony WH-1000XM4": "https://camelcamelcamel.com/product/B0863TXGM3",
    "Sony WH-1000XM5": "https://camelcamelcamel.com/product/B09XS7JWHH",
    "Bose NCH 700": "https://camelcamelcamel.com/product/B07Q9MJKBV",
}
price_limits = {
    "Sony WH-1000XM4": 280,
    "Sony WH-1000XM5": 350,
    "Bose NCH 700": 335,
}

for item, url in urls.items():
    price_limit = price_limits[item]
    backup_url = backup_urls[item]
    scraper = Scraper(url=url, price_limit=price_limit)
    price = scraper.scrapeAWS()
    if price is None:
        scraper.url = backup_url
        price = scraper.scrapeCamel()

    if scraper.priceCheck():
        print("emailing sale price")
        email = "zimmerj271@pm.me"
        subject = f"{item} on SALE for {price}!"
        message = url
        emailer = Emailer()
        emailer.sendEmail(email=email, subject=subject, message=message)
    else:
        print(f"Sale price is currently {price}")



