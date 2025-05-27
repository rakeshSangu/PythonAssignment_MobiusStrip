# Mobius Strip Geometry Calculator

This project models a 3D Möbius strip using parametric equations in Python and computes its **surface area** and **edge length** without using any external libraries.

## Features

- Generates a 3D mesh of points on a Möbius strip
- Approximates the surface area using triangle geometry
- Calculates the edge length numerically
- Written using only the built-in `math` module (no external libraries)

## Parametric Equations

The Möbius strip is defined using:

- x(u, v) = (R + v * cos(u / 2)) * cos(u)
- y(u, v) = (R + v * cos(u / 2)) * sin(u)
- z(u, v) = v * sin(u / 2)

Where:
- `u ∈ [0, 2π]`
- `v ∈ [-w/2, w/2]`
- `R`: Radius from center
- `w`: Width of the strip

## How It Works

1. Generates a grid of points across the Möbius strip surface.
2. Splits the surface into small squares and then into triangles.
3. Computes area using 3D cross product (determinant method).
4. Calculates edge length by summing distances along the boundaries.

## Usage

```bash
# Run the script
python mobius_strip.py
