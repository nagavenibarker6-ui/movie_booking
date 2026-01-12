from ticket import calculate_total_bill, booking_category

def test_total_bill_and_tickets():
    prices = [200, 300]
    quantities = [3, 2]
    total_bill, total_tickets = calculate_total_bill(prices, quantities)

    assert total_bill == 1200
    assert total_tickets == 5


def test_platinum_booking():
    assert booking_category(3500) == "Platinum Booking"


def test_gold_booking():
    assert booking_category(2000) == "Gold Booking"


def test_silver_booking():
    assert booking_category(1000) == "Silver Booking"
