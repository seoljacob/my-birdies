from playwright.sync_api import sync_playwright
import threading
import reserve
import util
from member import Member

def run(m):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        reserve.sign_in(page, m.email, m.phone_number)
        reserve.register(page, m.email, util.days_to_list(m.days))
        if m.guests and m.guest_days:
            reserve.add_guests(page, util.guests_to_list(m.guests), util.days_to_list(m.guest_days))
        browser.close()        

def main():
    emails = util.get_env_var("EMAILS")
    phone_numbers = util.get_env_var("PHONE_NUMBERS")
    days = util.get_env_var("DAYS")
    guests = util.get_env_var("GUESTS")
    guest_days = util.get_env_var("GUEST_DAYS")
    members = []
    for i in range(len(emails)):
        members.append(Member(emails[i], phone_numbers[i], days[i], guests[i], guest_days[i]))
    threads = []
    for member in members:
        t = threading.Thread(target=run, args=(member,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads: 
        t.join() 

if __name__=="__main__":
    main()
