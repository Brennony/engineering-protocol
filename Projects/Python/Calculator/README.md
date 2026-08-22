# Python Calculator

**Brennon York | Calculator Project**

A modular Python calculator built from the ground up to practice Python programming, mathematical logic, abstraction, testing, and software engineering principles.

---

## Current Version

**Calculator v1.3.1 - Implemented More Algebra Functions**

The calculator currently supports basic mathematical operations, algebraic functions, input validation, helper modules, and automated testing with `pytest`.

---

## Features

### Basic Mathematics

- Addition
- Subtraction
- Multiplication
- Division
- Remainder / Modulo
- Exponents
- Square roots
- Nth roots
- Floor
- Ceiling
- Absolute value
- Logarithms

### Algebra

- Slope
- Midpoint
- Distance between two points
- X-intercept
- Y-intercept
- Quadratic equations
- Quadratic roots
- Repeated quadratic roots
- Detection of quadratics with no real roots

### Input Validation

The calculator includes validation for mathematically invalid inputs, including:

- Division by zero
- Remainder by zero
- Square roots of negative numbers
- Zero as an nth-root index
- Invalid logarithm values
- Invalid logarithm bases
- Vertical lines with undefined slopes
- Invalid quadratic equations where `a = 0`

### Modular Architecture

The calculator is separated into multiple modules:

```text
Calculator
│
├── calculator.py
│
├── math_helpers.py
│
├── algebra_helpers.py
│
└── tests/
    ├── test_math_helpers.py
    └── test_algebra_helpers.py