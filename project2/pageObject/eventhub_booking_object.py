from playwright.sync_api import expect, Page


class EventHubBookingPage:
    def __init__(self, page: Page):
        self.page = page

    def select_event(self, event_name):
        self.page.locator('#nav-events').click()
        expect(self.page.get_by_role(role="heading",name="Upcoming Events")).to_be_visible()
        self.page.locator('select:has(option[value="Conference"])').select_option("Conference")

        event_card = self.page.get_by_role("heading", name=event_name).locator(
            "xpath=ancestor::div[.//a[@data-testid='book-now-btn']]"
        )
        book_now_btn = event_card.get_by_test_id("book-now-btn")
        expect(book_now_btn).to_be_visible(timeout=10000)
        book_now_btn.click()

        print(f"Clicked 'Book Now' for event '{event_name}'")




    def complete_booking(self, customer_name, email, phone):
        self.page.get_by_role("button", name="+").click()
        self.page.locator("#customerName").fill(customer_name)
        self.page.locator("#customer-email").fill(email)
        self.page.locator("#phone").fill(phone)
        self.page.get_by_role("button", name="Confirm Booking").click()
        expect(self.page.get_by_role(role="heading", name="Booking Confirmed! 🎉")).to_be_visible()
        print("Booking form submitted with customer details.")

    def verify_booking_result(self, expected):
        self.page.locator('#nav-bookings').click() 
        heading = self.page.get_by_role("heading", name="World Tech Summit").first
        expect(heading).to_be_visible()
        print("Booking confirmation heading is visible on the bookings page.")

