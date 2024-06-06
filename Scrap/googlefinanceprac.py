from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

url = 'https://www.google.com/finance/quote/Reliance:NSE'


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state("networkidle")
        page.evaluate("() => window.scroll(0,document.body.scrollHeight)")

        page.screenshot(path="Reliance.png", full_page=True)

        mainpage = page.inner_html("body")
        bs4html = BeautifulSoup(mainpage, "html.parser")
        print(bs4html)
        