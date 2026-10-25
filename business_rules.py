# Business rule constants
SERVICE_FEE = 75.00
SMALL_EVENT_LIMIT = 25
MEDIUM_EVENT_LIMIT = 100
SMALL_EVENT_DISCOUNT = 0.05
NONPROFIT_LARGE_DISCOUNT = 0.12
SERVICE_FEE_THRESHOLD = 500.00


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Calculate the food cost before discounts and fees."""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the discount rate for an event."""
    if guests < SMALL_EVENT_LIMIT:
        return 0.0
    if guests < MEDIUM_EVENT_LIMIT:
        return SMALL_EVENT_DISCOUNT
    if nonprofit:
        return NONPROFIT_LARGE_DISCOUNT
    return SMALL_EVENT_DISCOUNT


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Calculate the final event total after discounts and service fee."""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    discounted_cost = round(food_cost * (1 - discount), 2)

    if discounted_cost <= SERVICE_FEE_THRESHOLD:
        discounted_cost += SERVICE_FEE

    return round(discounted_cost, 2)


# Approval and staffing thresholds
SIGNOFF_THRESHOLD = 2500.00
SECOND_CHEF_GUEST_THRESHOLD = 80
SECOND_CHEF_TOTAL_THRESHOLD = 3000.00


def needs_signoff(total: float) -> bool:
    """Return whether an event requires sign-off."""
    return total > SIGNOFF_THRESHOLD


def needs_second_chef(guests: int, total: float) -> bool:
    """Return whether an event requires a second chef."""
    return guests > SECOND_CHEF_GUEST_THRESHOLD or total >= SECOND_CHEF_TOTAL_THRESHOLD


def total_booked(events: list) -> float:
    """Calculate the total value of all booked events."""
    total = 0.0
    for event in events:
        total += calculate_event_total(
            event["guest_price"],
            event["guests"],
            event["nonprofit"],
        )
    return round(total, 2)


def largest_event(events: list) -> str:
    """Return the client name of the event with the largest total."""
    largest_client = ""
    largest_total = -1.0

    for event in events:
        event_total = calculate_event_total(
            event["guest_price"],
            event["guests"],
            event["nonprofit"],
        )
        if event_total > largest_total:
            largest_total = event_total
            largest_client = event["client"]

    return largest_client


def format_event_line(
    client: str,
    total: float,
    signoff: bool,
    second_chef: bool,
) -> str:
    """Format an event's details as one report line."""
    signoff_text = "yes" if signoff else "no"
    chef_text = "yes" if second_chef else "no"
    return (
        f"{client}: ${total:.2f} | sign-off: {signoff_text} | second chef: {chef_text}"
    )
