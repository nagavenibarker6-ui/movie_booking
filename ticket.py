import sys
PROGRAM_NAME = "Movie Ticket Booking System"
def calculate_total_bill(prices, quantities):
    total_bill = 0
    total_tickets = 0
    for p, q in zip(prices, quantities):
        total_bill += p * q
        total_tickets += q
    return total_bill, total_tickets
def booking_category(total_bill):
    if total_bill >= 3000:
        return "Platinum Booking"
    elif 1500 <= total_bill <= 2999:
        return "Gold Booking"
    else:
        return "Silver Booking"
def main():
    customer_name = "Nagaveni"
    movie_name = "Inception"
    ticket_prices = [200, 300]
    ticket_quantities = [3, 2]
    if len(sys.argv) == 5:
        customer_name = sys.argv[1]
        movie_name = sys.argv[2]
        ticket_prices = list(map(int, sys.argv[3].split(",")))
        ticket_quantities = list(map(int, sys.argv[4].split(",")))
    total_bill, total_tickets = calculate_total_bill(
        ticket_prices, ticket_quantities
    )
    category = booking_category(total_bill)
    print("Program Name:", PROGRAM_NAME)
    print("Customer Name:", customer_name)
    print("Movie Name:", movie_name)
    print("Ticket Prices:", ticket_prices)
    print("Ticket Quantities:", ticket_quantities)
    print("Total Tickets Booked:", total_tickets)
    print("Total Bill Amount: ", total_bill)
    print("Booking Category:", category)
if __name__ == "__main__":
    main()
