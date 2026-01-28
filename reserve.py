from playwright.sync_api import sync_playwright
import time

def main():
    print("Hello, World!")

if __name__=="__main__":
    main()

#with sync_playwright() as p:
#    browser = p.chromium.launch(headless=False, slow_mo=100)
#    page = browser.new_page()
#    page.goto("https://mybirdies.ca")
#    print(page.title())
#    sign_in = page.get_by_role("link", name="Sign In").click()
#    page.get_by_placeholder("you@example.com").fill("jacobseol96@gmail.com")
#    page.get_by_role("button", name="Continue").click()
#    page.get_by_placeholder("7781234567").fill("2365136930")
#    page.get_by_role("button", name="Sign In").click()
#    page.get_by_text("Monday").click()
#    page.get_by_role("button", name="Register Now").click()
#    time.sleep(3000) 
#    browser.close()
#
