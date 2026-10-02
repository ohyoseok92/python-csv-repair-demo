# Python CSV Empty-Row Repair Demo

A minimal, dependency-free example of turning a reproducible CSV parsing failure into a tested repair.

This is a self-produced demonstration, not paid client work. It supports the Python & Browser Automation Rescue — 6-Hour Sprint. [Review the scope and request a fit check before payment](https://payhip.com/b/yUF4Q).

## The failure

The legacy parser converts every row directly to an integer. A blank row therefore raises `ValueError` and stops the workflow.

```python
return [int(row) for row in text.splitlines()]
```

## The repair

The corrected parser trims each row, skips only blank rows, and still raises an error for non-empty invalid input. This avoids hiding real data problems.

## Verification

Run from this directory with Python 3.9 or newer:

```powershell
python -m unittest -v test_csv_repair.py
```

Expected result: three tests pass. The first test preserves the original crash as expected evidence; the second verifies the repair; the third confirms that non-empty invalid input is not silently discarded.

```text
Ran 3 tests

OK
```

## Files

- `csv_repair.py`: failing legacy implementation and repaired implementation
- `test_csv_repair.py`: regression tests for the failure, repair, and invalid-input boundary

## Before requesting a scope review

A short, redacted example helps me decide whether the issue fits one six-hour sprint. Please include:

- The Python/library or browser tool and version, plus the expected and actual result.
- The smallest steps and sample input that reproduce the failure; include the exact error if there is one.
- The output format you need, any behavior that must stay unchanged, and your deadline/time zone.

Remove passwords, API keys, payment details, and personal or customer data. A fictional sample is fine for the first review. I confirm the definition of done and whether the USD 99 fixed-price scope fits **before** you pay. If it does not fit, I will describe a smaller possible first milestone rather than promise a full repair in six hours.

## Need help with a broken automation?

The fixed-price rescue sprint covers one reproducible Python or permitted browser-automation failure, including diagnosis, the agreed change, repeatable verification, and concise handoff notes. [Review the scope and request a fit check before payment](https://payhip.com/b/yUF4Q). If the agreed scope is clear, [order through Ko-fi](https://ko-fi.com/c/36789bd8ca?utm_source=github&utm_medium=repository&utm_campaign=conversion_v3&utm_content=csv_repair_demo).
