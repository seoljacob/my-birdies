from playwright.sync_api import expect

def sign_in(p, e, ph):
    try:
        p.goto("https://mybirdies.ca")
        p.get_by_role("link", name="Sign In").click()
        p.get_by_placeholder("you@example.com").fill(e)
        p.get_by_role("button", name="Continue").click()
        p.get_by_placeholder("7781234567").fill(ph)
        p.get_by_role("button", name="Sign In").click()
    except Exception as err:
        print("Could not sign in.")
        print(str(err))

def register(p, e, d):
    for day in d:
        try:
            print(f"Registering {e} for {day}...")
            expect(p.get_by_text(day)).to_be_visible()
            p.get_by_text(day).click()
            expect(p.get_by_role("button", name="Register Now")).to_be_visible()
            p.get_by_role("button", name="Register Now").click()
            print(f"Registered {e} for {day}!")
        except Exception as err:
            print(f"Could not register {e} for {day}.")
            print(str(err))
        finally:
            p.get_by_text("Birdie Buddies").click()

def add_guests(p, g, gd):
    for guest in g:
        for day in gd:
            try:
                print(f"Adding {guest} for {day}...")
                expect(p.get_by_text(day)).to_be_visible()
                p.get_by_text(day).click()
                expect(p.get_by_placeholder("Guest name")).to_be_visible()
                p.get_by_placeholder("Guest name").fill(g)
                expect(p.get_by_role("button", name="Add")).to_be_visible()
                p.get_by_role("button", name="Add").click()
                print(f"Added {guest} for {day}!")
            except Exception as err:
                print(f"Could not add {guest} for {day}")
                print(str(err))
            finally:
                p.get_by_text("Birdie Buddies").click()
