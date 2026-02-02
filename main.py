from playwright.sync_api import sync_playwright
import os
import threading
import reserve
import util
from member import Member

def run(m):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        reserve.sign_in(page, m.email, m.phone_number)
        reserve.register(page, util.map_str_to_list(m.days))
        browser.close()        

def main():
    emails = util.get_env_var("EMAILS")
    phone_numbers = util.get_env_var("PHONE_NUMBERS")
    days = util.get_env_var("DAYS")
    members = []
    for i in range(len(emails)):
        members.append(Member(emails[i], phone_numbers[i], days[i]))
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
