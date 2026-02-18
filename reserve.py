from playwright.sync_api import expect
import time

def retry(p, fn, t=10):
    end_time = time.time() + t
    i = 1
    success = False
    while time.time() < end_time:
        if not fn():
            print(f"Retrying ({i})...")
            p.reload()
            i += 1
        else:
            success = True
            break
    return success

def click_element(p, locator_fn, locator_arg, description, timeout=500):
    try:
        locator = locator_fn(locator_arg)
        expect(locator).to_be_visible(timeout=timeout)
        locator.click()
        print(f"Clicked {description}!")
        return True
    except Exception:
        print(f"Could not click {description}.")
        return False

def click_day(p, d):
    return click_element(p, p.get_by_text, d, d)

def click_register(p, s):
    return click_element(p, lambda name: p.get_by_role("button", name=name), s, s)

def sign_in(p, e, ph):
    try:
        p.goto("https://mybirdies.ca")
        p.get_by_role("link", name="Sign In").click()
        p.get_by_placeholder("you@example.com").fill(e)
        p.get_by_role("button", name="Continue").click()
        p.get_by_placeholder("7781234567").fill(ph)
        p.get_by_role("button", name="Sign In").click()
    except Exception:
        print("Could not sign in.")

def register(p, e, d):
    for day in d:
        try:
            print(f"Registering {e} for {day}...")
            if not retry(p, lambda: click_day(p, day)):
                raise Exception()
            if not click_register(p, "Register Now"):
                raise Exception()
            print(f"Registered {e} for {day}!")
        except Exception:
            print(f"Could not register {e} for {day}.")
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
