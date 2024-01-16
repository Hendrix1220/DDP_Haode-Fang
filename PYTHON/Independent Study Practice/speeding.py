def speeding_ticket(speed, is_birthday):
    if is_birthday==True:
        if speed<=65:
            return "No Ticket"
        elif speed<=85:
            return "Small Ticket"
        else: return "Big Ticket"
    else:
        if speed<=60:
            return "No Ticket"
        elif speed<=80:
            return "Small Ticket"
        else: return "Big Ticket"
    # Your code goes here
    pass


# Test cases
print(speeding_ticket(60, False))  # Expected output: "No Ticket"
print(speeding_ticket(75, False))  # Expected output: "Small Ticket"
print(speeding_ticket(85, False))  # Expected output: "Big Ticket"
print(speeding_ticket(65, True))  # Expected output: "No Ticket"
print(speeding_ticket(85, True))  # Expected output: "Small Ticket"