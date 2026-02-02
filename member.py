class Member:
    def __init__(self, e, ph, d, g=False):
        self.email = e
        self.phone_number = ph
        self.days = d
        self.has_guests = g

    def __str__(self):
        return f"""Email: {self.email}
        Phone number: {self.phone_number}
        Days: {self.days}
        Guests? {self.has_guests}"""
