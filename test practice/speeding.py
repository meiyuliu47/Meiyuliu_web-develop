def speeding_ticket(speed, is_birthday):
    # Define speed limits based on birthday condition
    no_ticket_limit = 65 if is_birthday else 60
    small_ticket_limit = 80 if is_birthday else 75
    
    # Evaluate the driver's speed and return the appropriate ticket category
    if speed <= no_ticket_limit:
        return "No Ticket"
    elif speed <= small_ticket_limit:
        return "Small Ticket"
    else:
        return "Big Ticket"

print(speeding_ticket(75, False)) 
