import os
import asyncio
from playwright.async_api import async_playwright

email = os.getenv("email")
senha = os.getenv("senha")


async def get_skills(link):
    async with async_playwright() as play:
        browser = await play.chromium.launch(headless=False)
        page = await browser.new_page()
        
        await page.goto(link)
        
        await page.wait_for_selector("button[data-modal='base-sign-in-modal']", timeout=5000)
        await page.click("button[data-modal='base-sign-in-modal']")
        
        await page.fill("input#base-sign-in-modal_session_key", f"{email}")
        await page.fill("input#base-sign-in-modal_session_password", f"{senha}")
        
        await page.click("button:text('Entrar')[type='submit']")
        
        await asyncio.sleep(10)
        
        await browser.close()
        
asyncio.run(get_skills("https://www.linkedin.com/jobs/search/?currentJobId=4114551949&distance=25&geoId=106057199&keywords=python&origin=JOBS_HOME_SEARCH_CARDS"))