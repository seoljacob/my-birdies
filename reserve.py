from playwright.sync_api import sync_playwright
import time

def sign_in(p):
    try:
        p.goto("https://mybirdies.ca")
        p.get_by_role("link", name="Sign In").click()
        p.get_by_placeholder("you@example.com").fill("jacobseol96@gmail.com")
        p.get_by_role("button", name="Continue").click()
        p.get_by_placeholder("7781234567").fill("2365136930")
        p.get_by_role("button", name="Sign In").click()
    except Error as e:
        print(f"{type(e).__name__}: {e}")

def register(p, days):
    for day in days:
        try:
            print(f"Registering for {day}")
            #p.get_by_text(day).click()
            #p.get_by_role("button", name="Register Now").click()
            #p.get_by_text("Birdie Buddies").click()
        except Error as e:
            print(f"{type(e).__name__}: {e}")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        sign_in(page)
        register(page, ["Monday", "Wednesday"])
        browser.close()        

if __name__=="__main__":
    main()


