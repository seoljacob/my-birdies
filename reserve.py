from decimal import Decimal
from playwright.sync_api import expect
import re
import time


def click_element(locator_fn, locator_arg, timeout=500):
    try:
        locator = locator_fn(locator_arg)
        expect(locator).to_be_visible(timeout=timeout)
        locator.click()
        return True
    except Exception as err:
        print(f"Could not click {locator_arg}.")
        return False

def click_button(p, s):
    return click_element(lambda name: p.get_by_role("button", name=name), s)

def click_card(p, d):
    return click_element(p.get_by_text, d)

def is_balance_sufficient(p, e, n):
    try:
        title = "Available balance - Click to view wallet"
        expect(p.get_by_title(title)).to_have_text(re.compile(r"\$\d+\.\d{2}"))
        balance = p.get_by_title(title).text_content().strip()
        balance = Decimal(balance[1:])
        cost = 15.00
        balance_needed = cost * n
        if balance < balance_needed:
            print(f"{e} has insufficient balance: ${balance:.2f}")
            return False
        return True
    except Exception as err:
        print(f"Could not check balance for {e}: {err}")
    
def retry(p, fn, t=120):
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

def sign_in(p, e, ph):
    try:
        p.goto("https://mybirdies.ca/login")
        p.get_by_placeholder("name@example.com").fill(e)
        click_button(p, "Continue with Email")
        p.get_by_placeholder("7781234567").fill(ph)
        click_button(p, "Sign In")
        return True
    except Exception:
        print(f"Could not sign in.")
        return False

def register(p, e, d):
    try:
        print(f"Registering {e} for {d}...")
        if not retry(p, lambda: click_card(p, d)):
            raise Exception()
        if not retry(p, lambda: click_button(p, "Register Now")):
            raise Exception()
        p.wait_for_timeout(5000)
        print(f"Registered {e} for {d}!")
    except Exception:
        print(f"Could not register {e} for {d}.")
    finally:
        p.goto("https://mybirdies.ca/sessions")
