# Python Calculator

**Brennon York | Calculator Project**

A modular Python calculator built from the ground up to practice Python programming, mathematical logic, abstraction, testing, and software engineering principles.

---

## Current Version

**Calculator V1.3.4**

The calculator supports basic mathematical operations, algebraic functions, trigonometric functions, a settings system, calculation history, mathematical constants, and a full automated test suite with `pytest`.

---

## Features

### Basic Mathematics

- Addition, Subtraction, Multiplication, Division
- Remainder / Modulo
- Exponents
- Square roots, Nth roots
- Floor, Ceiling, Absolute value
- Logarithms

### Algebra

- Slope, Midpoint, Distance between two points
- X-intercept, Y-intercept
- Quadratic equations (real roots, repeated roots, no real roots detection)

### Trigonometry

- Sine, Cosine, Tangent
- Secant, Cosecant, Cotangent
- Arc Sine, Arc Cosine, Arc Tangent
- Degree / Radian mode toggle via Settings
- Undefined case detection with clean messaging

### Mathematical Constants

Supports named constant input — type instead of typing the raw value:

- `pi` → π
- `e` → e
- `tau` → τ

Constants are also recognized in output for clean display formatting.

### Calculation History

- Stores up to 100 previous calculations
- Accessible via the Settings menu
- Reference the last result in any new calculation by typing `ans`

### Settings

- Toggle between Radians and Degrees mode for trigonometric operations
- View full calculation history

### Smart Output Formatting

- Results close to zero display as `0`
- Results close to whole numbers are rounded cleanly
- Results matching known constants display as symbols (`π`, `e`, `τ`)

### Input Validation

The calculator validates all mathematically invalid inputs, including:

- Division or remainder by zero
- Square roots of negative numbers
- Zero as an nth-root index
- Invalid logarithm values and bases
- Vertical lines with undefined slopes
- Quadratics where `a = 0`
- Trig functions at undefined angles (returns clean undefined message)
- Arc functions outside valid domain `[-1, 1]`

---

## Modular Architecture

```text
Calculator/
│
├── calculator.py
│
├── math_helpers.py
├── algebra_helpers.py
├── trig_helpers.py
│
└── tests/
    ├── test_math_helpers.py
    ├── test_algebra_helpers.py
    └── test_trig_helpers.py
```

---

## Testing

All helper modules are covered by automated tests using `pytest`.

Run the full test suite from the `Calculator/` directory:

```bash
python -m pytest tests/ -v
```

**Current test results: 40/40 passing**

---

## Planned Future Versions

- **v1.4** — Regular expressions, multi-operation calculations
- **v1.5** — Calculus capabilities (numerical integration, derivatives)

---

## Built With

- Python 3.13
- `math` module
- `pytest`