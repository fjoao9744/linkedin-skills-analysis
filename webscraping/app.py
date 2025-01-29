import os
import asyncio
from playwright.async_api import async_playwright

email = os.getenv("email")
senha = os.getenv("senha")

async def reformat_string(string):
    new_string = []
    palavra = ""
    for word in string.replace("\n", " | ").split():
        palavra += f" {word}"
        if word == "|":
            palavra = palavra.replace(" |", "").strip()
            if not palavra == "Adicionar":
                new_string.append(palavra)
                palavra = ""
            palavra = ""

    return new_string

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
        
        await page.wait_for_selector('xpath=/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul')
        
        ul = page.locator('xpath=/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul')
        
        lis = ul.locator("li strong")
        li_count = await lis.count()
                
        for i in range(li_count):
            await page.wait_for_selector('xpath=/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[6]/section[2]/div/button/span')
            await page.locator('xpath=/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[6]/section[2]/div/button/span').click()
            
            await page.wait_for_selector('xpath=/html/body/div[4]/div/div/div[2]/div/div[1]/ul')
            competencias = page.locator('xpath=/html/body/div[4]/div/div/div[2]/div/div[1]/ul')
            competencia = competencias.locator("li")
            competencia_count = await competencia.count()
            
            for c in range(competencia_count):
                competencia_texto = await competencias.nth(c).inner_text()
                
                print(await reformat_string(competencia_texto))
                break
                
            await page.locator('xpath=/html/body/div[4]/div/div/div[3]/button/span').click()
            
            await lis.nth(i).click()
            
            
        

            
        await asyncio.sleep(30)
        
        await browser.close()
        
asyncio.run(get_skills("https://www.linkedin.com/jobs/", "Javascript"))

