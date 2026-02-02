from playwright.sync_api import expect

def sign_in(p, e, ph):
    try:
        p.goto("https://mybirdies.ca")
        p.get_by_role("link", name="Sign In").click()
        p.get_by_placeholder("you@example.com").fill(e)
        p.get_by_role("button", name="Continue").click()
        p.get_by_placeholder("7781234567").fill(ph)
        p.get_by_role("button", name="Sign In").click()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

def register(p, d):
    for day in d:
        try:
            print(f"Registering for {day}...")
            p.get_by_text(day).click()
            expect(p.get_by_role("button", name="Register Now")).to_be_visible()
            p.get_by_role("button", name="Register Now").click()
            print(f"Registered for {day}!")
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
        finally:
            p.get_by_text("Birdie Buddies").click()
