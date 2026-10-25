
# Terminal Record: Harvest Table Catering

## 1. Building the project

Command:
```bash
pwd
```

Output:
```text
/home/fouzan/ism3232-midterm
```

Command:
```bash
mkdir -p tests
```

Output:
```text
Directory created or already exists.
```

The project directory contains the Python business rules, report program, automated tests, dependency list, and documentation. The `tests/` directory holds the automated test suite.

## 2. The virtual environment

Command:
```bash
which python3
```

Output:
```text
/home/fouzan/ism3232-midterm/.venv/bin/python3
```

The path confirms that Python is running from the project's virtual environment.

## 3. The project structure

Command:
```bash
tree -L 2
```

Output:
```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The `.venv` directory is hidden and therefore does not appear in this output. The `__pycache__` directories contain Python-generated cache files and are excluded from Git tracking by `.gitignore`.

## 4. Every function and test

Command:
```bash
rg 'def ' business_rules.py tests/test_business_rules.py
```

Output:
```text
tests/test_business_rules.py
11:def test_calculate_food_cost_multiplies_price_by_guests():
15:def test_calculate_food_cost_with_zero_guests():
19:def test_get_event_discount_below_25_guests():
23:def test_get_event_discount_at_25_guests():
27:def test_get_event_discount_at_99_guests():
31:def test_get_event_discount_at_100_guests_for_regular_client():
35:def test_get_event_discount_at_100_guests_for_nonprofit():
39:def test_get_event_discount_large_nonprofit():
43:def test_calculate_event_total_without_discount():
47:def test_calculate_event_total_with_discount_and_service_fee():
51:def test_calculate_event_total_with_discount_without_service_fee():
55:def test_calculate_event_total_nonprofit_large_event():
62:def test_needs_signoff_below_threshold():
66:def test_needs_signoff_at_threshold():
70:def test_needs_signoff_above_threshold():
74:def test_needs_second_chef_at_80_guests_below_total_threshold():
78:def test_needs_second_chef_above_80_guests():
82:def test_needs_second_chef_at_3000_total():
86:def test_needs_second_chef_below_3000_total():
93:def test_total_booked_with_two_events():
111:def test_total_booked_with_empty_list():
115:def test_largest_event_returns_highest_total():
133:def test_largest_event_tie_returns_first_event():
151:def test_largest_event_with_empty_list():
155:def test_format_event_line_with_no_approvals():
160:def test_format_event_line_with_both_approvals():
165:def test_calculate_event_total_at_service_fee_threshold():
171:def test_calculate_event_total_above_service_fee_threshold():

business_rules.py
12:def calculate_food_cost(guest_price: float, guests: int) -> float:
17:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
28:def calculate_event_total(
48:def needs_signoff(total: float) -> bool:
53:def needs_second_chef(guests: int, total: float) -> bool:
58:def total_booked(events: list) -> float:
70:def largest_event(events: list) -> str:
88:def format_event_line(
```

The output lists eight business-rule functions and 28 test functions. The tests cover the required functions, business-rule thresholds, and edge cases.

## 5. Which files print

Command:
```bash
rg -l 'print' .
```

Output:
```text
./commands.md
./main.py
./README.md
```

`main.py` prints the event report. The matches in `commands.md` and `README.md` are documentation text. `business_rules.py` is not listed because it contains no `print` calls.

## 6. The commit history

Command:
```bash
git log --oneline

Output:
```text
dc356b4 docs: record terminal commands and verification
771d802 feat: generate catering event report
edf6978 test: cover catering business rules and boundaries
f7c8817 feat: implement catering business rules
d7ddd66 docs: add project README
4e7a295 chore: add project ignore rules and dependencies```

The repository currently contains five commits covering project setup, documentation, business logic, tests, and the event report. Additional documentation and verification commits will be recorded as the project is finalized.

## 7. Final verification

Commands:
```bash
pytest -v
ruff check .
git status --short

Results:
- All 28 tests passed.
- Ruff reported no issues.
- The working tree was clean before this final documentation update.
