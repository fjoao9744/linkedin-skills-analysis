import os
import asyncio
from playwright.async_api import async_playwright

email = os.getenv("email")
senha = os.getenv("senha")

async def get_skills(link, keyword):
    async with async_playwright() as play:
        browser = await play.chromium.launch(headless=False)
        page = await browser.new_page()
        
        await page.goto(link)
        
        # await page.wait_for_selector("button[data-modal='base-sign-in-modal']", timeout=5000)
        # await page.click("button[data-modal='base-sign-in-modal']")
        
        await page.fill("input#session_key", f"{email}")
        await page.fill("input#session_password", f"{senha}")
        
        await page.press("input#session_password", "Enter")
        
        await page.wait_for_selector("input[id^=jobs-search-box-keyword-id]")
        
        await page.fill("input[id^=jobs-search-box-keyword-id]",
                        keyword)
        
        await page.press("input[id^=jobs-search-box-keyword-id]", "Enter")
        
        await asyncio.sleep(10)
        
        await browser.close()
        
asyncio.run(get_skills("https://www.linkedin.com/jobs/", "Javascript"))

