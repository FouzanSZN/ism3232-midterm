"""Tests for Harvest Table Catering business rules."""

from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
)


def test_calculate_food_cost_multiplies_price_by_guests():
    assert calculate_food_cost(20.00, 10) == 200.00


def test_calculate_food_cost_with_zero_guests():
    assert calculate_food_cost(20.00, 0) == 0.00


def test_get_event_discount_below_25_guests():
    assert get_event_discount(24) == 0.0


def test_get_event_discount_at_25_guests():
    assert get_event_discount(25) == 0.05


def test_get_event_discount_at_99_guests():
    assert get_event_discount(99) == 0.05


def test_get_event_discount_at_100_guests_for_regular_client():
    assert get_event_discount(100, nonprofit=False) == 0.05


def test_get_event_discount_at_100_guests_for_nonprofit():
    assert get_event_discount(100, nonprofit=True) == 0.12


def test_get_event_discount_large_nonprofit():
    assert get_event_discount(150, nonprofit=True) == 0.12


def test_calculate_event_total_without_discount():
    assert calculate_event_total(20.00, 20) == 475.00


def test_calculate_event_total_with_discount_and_service_fee():
    assert calculate_event_total(20.00, 25) == 550.00


def test_calculate_event_total_with_discount_without_service_fee():
    assert calculate_event_total(20.00, 30) == 570.00


def test_calculate_event_total_nonprofit_large_event():
    assert calculate_event_total(10.00, 100, nonprofit=True) == 880.00


def test_needs_signoff_below_threshold():
    assert needs_signoff(2499.99) is False


def test_needs_signoff_at_threshold():
    assert needs_signoff(2500.00) is False


def test_needs_signoff_above_threshold():
    assert needs_signoff(2500.01) is True


def test_needs_second_chef_at_80_guests_below_total_threshold():
    assert needs_second_chef(80, 2000.00) is False


def test_needs_second_chef_above_80_guests():
    assert needs_second_chef(81, 2000.00) is True


def test_needs_second_chef_at_3000_total():
    assert needs_second_chef(50, 3000.00) is True


def test_needs_second_chef_below_3000_total():
    assert needs_second_chef(50, 2999.99) is False


def test_total_booked_with_two_events():
    events = [
        {
            "client": "Alpha",
            "guest_price": 20.00,
            "guests": 20,
            "nonprofit": False,
        },
        {
            "client": "Beta",
            "guest_price": 20.00,
            "guests": 25,
            "nonprofit": False,
        },
    ]
    assert total_booked(events) == 1025.00


def test_total_booked_with_empty_list():
    assert total_booked([]) == 0.00


def test_largest_event_returns_highest_total():
    events = [
        {
            "client": "Alpha",
            "guest_price": 20.00,
            "guests": 20,
            "nonprofit": False,
        },
        {
            "client": "Beta",
            "guest_price": 30.00,
            "guests": 100,
            "nonprofit": False,
        },
    ]
    assert largest_event(events) == "Beta"


def test_largest_event_tie_returns_first_event():
    events = [
        {
            "client": "Alpha",
            "guest_price": 20.00,
            "guests": 20,
            "nonprofit": False,
        },
        {
            "client": "Beta",
            "guest_price": 20.00,
            "guests": 20,
            "nonprofit": False,
        },
    ]
    assert largest_event(events) == "Alpha"


def test_largest_event_with_empty_list():
    assert largest_event([]) == ""


def test_format_event_line_with_no_approvals():
    result = format_event_line("Finch Law", 435.0, False, False)
    assert result == "Finch Law: $435.00 | sign-off: no | second chef: no"


def test_format_event_line_with_both_approvals():
    result = format_event_line("Hilltop Gym", 3420.0, True, True)
    assert result == "Hilltop Gym: $3420.00 | sign-off: yes | second chef: yes"


def test_calculate_event_total_at_service_fee_threshold():
    guest_price = 500 / (25 * 0.95)

    assert calculate_event_total(guest_price, 25) == 575.00


def test_calculate_event_total_above_service_fee_threshold():
    guest_price = 500.01 / (25 * 0.95)

    assert calculate_event_total(guest_price, 25) == 500.01
