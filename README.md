# ISM3232 Midterm: Harvest Table Catering

- **Name:** Fouzan Haider
- **Version:** 1.0.0
- **Date:** October 25, 2026

## What This Program Does

This Python program calculates catering event totals for Harvest Table Catering. It applies discounts and service fees, determines whether an event needs management sign-off or a second chef, and prints a report summarizing all booked events.

## Business Rules

- Food cost is calculated by multiplying the price per guest by the number of guests.
- Events with fewer than 25 guests receive no discount.
- Events with 25–99 guests receive a 5% discount.
- Events with 100 or more guests receive a 12% discount if they are nonprofit events; other events receive 5%.
- A $75 service fee applies when the discounted cost is $500 or less.
- Events totaling more than $2,500 require sign-off.
- Events with more than 80 guests or a total of at least $3,000 require a second chef.

## How to Run

Activate the project's virtual environment, then run:

```bash
python3 main.py
```

## How to Test

Run the test suite with:

```bash
pytest -v
```

Check code quality and formatting with:

```bash
ruff check .
ruff format .
```

## Files in This Repository

- `business_rules.py` — Functions that implement the catering business rules.
- `main.py` — Sample events and the event summary report.
- `tests/test_business_rules.py` — Automated tests for the required functions and boundary conditions.
- `tests/__init__.py` — Makes the tests directory a Python package.
- `commands.md` — Terminal commands and their recorded outputs.
- `requirements.txt` — Python package dependencies.
- `.gitignore` — Excludes the virtual environment and Python cache files.

## AI Use Statement

Not used
