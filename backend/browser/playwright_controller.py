from playwright.async_api import async_playwright


async def google_search(query: str):

    try:

        # START PLAYWRIGHT
        p = await async_playwright().start()

        # OPEN REAL CHROME
        browser = await p.chromium.launch(
            channel="chrome",
            headless=False,
            slow_mo=120,
            args=[
                "--disable-blink-features=AutomationControlled"
            ]
        )

        # CREATE BROWSER CONTEXT
        context = await browser.new_context(
            viewport={
                "width": 1400,
                "height": 900
            },
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/136.0.0.0 Safari/537.36"
            )
        )

        # CREATE PAGE
        page = await context.new_page()

        # REMOVE PLAYWRIGHT DETECTION
        await page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        """)

        print(f"\\nSearching Google for: {query}")

        # OPEN GOOGLE
        await page.goto(
            "https://www.google.com",
            wait_until="domcontentloaded"
        )

        # HUMAN-LIKE WAIT
        await page.wait_for_timeout(2000)

        # TYPE QUERY
        await page.fill(
            'textarea[name="q"]',
            query
        )

        await page.wait_for_timeout(1000)

        # PRESS ENTER
        await page.keyboard.press("Enter")

        # WAIT FOR RESULTS
        await page.wait_for_load_state("networkidle")

        # PAGE TITLE
        title = await page.title()

        print(f"\\nSearch Completed: {title}")

        print("\\nAURA Browser Agent Active...")
        print("Close browser manually when finished.")

        # KEEP BROWSER OPEN FOREVER
        while True:
            await page.wait_for_timeout(1000)

    except Exception as e:

        print(f"\\nBrowser Error: {e}")

        return "Browser session ended."