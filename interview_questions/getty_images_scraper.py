import asyncio
from urllib.parse import urlencode

from playwright.async_api import BrowserContext, async_playwright

"""
Kalepa; Senior Full Stack Engineer Interview Question

https://www.glassdoor.com/Interview/Kalepa-Interview-Questions-E2322243.htm

Content: Was asked to use beautifulsoup4 to scrape images from Getty Images website. Images seem to be loaded dynamically and require Javascript to be executed... (Used playwright to solve this)
"""


async def fetch_images_from_page(
    ctx: BrowserContext, search_url: str, page_number: int
) -> list[str]:
    query_string = urlencode({"page": page_number})
    page = await ctx.new_page()
    await page.goto(f"{search_url}?{query_string}")
    await page.wait_for_selector("img")

    images = await page.query_selector_all("a > figure > picture > img")
    image_urls = [
        await img.get_attribute("src")
        for img in images
        if await img.get_attribute("src")
    ]

    print(f"Processed page {page_number} ⛏️")
    return image_urls


async def search_getty_images(search_phrase: str, num_pages: int) -> list[str]:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()

        search_url = (
            f"https://www.gettyimages.com/photos/{search_phrase.replace(' ', '-')}"
        )

        tasks = [
            fetch_images_from_page(
                context,
                search_url,
                page_number,
            )
            for page_number in range(1, num_pages + 1)
        ]
        results = await asyncio.gather(*tasks)

        image_urls = [url for sublist in results for url in sublist]

        await browser.close()
        return image_urls


async def main() -> None:
    search_word = input("Enter the search phrase: ").replace(" ", "-")
    num_pages = int(input("Enter the max number of pages to scrape: "))
    await search_getty_images(search_word, num_pages)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
