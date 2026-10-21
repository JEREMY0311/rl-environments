# invoice-discounts

## Task given to the agent

Apply the agreed discount to every line of the invoice. Return the final price of each
line and the invoice total, in PEN, with two decimals.

## Environment

Initial state is `fixtures/input.json`. Money is given as decimal strings (`"100.00"`),
never as floats. Discounts are whole percentages.

| line | precio | dto | exact final |
|------|--------|-----|-------------|
| L-01 | 100.00 | 10% | 90.00 |
| L-02 | 1.00   | 50% | 0.50 |
| L-03 | 10.00  | 33% | 6.70 |
| L-04 | 250.00 | 20% | 200.00 |

Exact total: **297.20**

## Output contract

```json
{"lines": [{"id": "L-01", "final": "90.00"}, ...], "total": "297.20"}
```

## What the verifier must do

Expose, in `verify.py`:

```python
def verify(output: dict, input: dict) -> int
```

Return `1` only if the output is correct. Return `0` otherwise. No human in the loop,
no tolerance, no "close enough".

Run the attacks with:

```
python3 tests/run_tests.py
```
