#!/usr/bin/env python3
"""Corre los cinco ataques contra tu verify.py

    python3 tests/run_tests.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def load(name):
    return json.loads((ROOT / "fixtures" / f"{name}.json").read_text(encoding="utf-8"))


CASES = [
    ("attempt_1", 0, "division entera: L-02 y L-03 estan mal"),
    ("attempt_2", 1, "correcto"),
    ("attempt_3", 0, "borro L-02 y L-03; las lineas que quedan SI estan bien"),
    ("attempt_4", 0, "invento la linea L-05; su total cuadra con sus propias lineas"),
    ("attempt_5", 0, "lineas correctas, pero el total declarado no es la suma"),
]


def main():
    try:
        from verify import verify
    except ImportError:
        print("No encuentro verify.py con una funcion verify(output, input).")
        print("Creala en environments/invoice-discounts/verify.py")
        return 1

    inp = load("input")
    failed = 0
    for name, expected, why in CASES:
        try:
            got = verify(load(name), inp)
        except Exception as exc:
            print(f"FALLA  {name}: lanzo {type(exc).__name__}: {exc}")
            failed += 1
            continue
        if got not in (0, 1):
            print(f"FALLA  {name}: verify debe devolver 0 o 1, devolvio {got!r}")
            failed += 1
        elif got != expected:
            print(f"FALLA  {name}: esperaba {expected}, devolvio {got}  ->  {why}")
            failed += 1
        else:
            print(f"ok     {name}  ->  {got}")

    print()
    print("TODO VERDE" if failed == 0 else f"{failed} de {len(CASES)} fallando")
    return 1 if failed else 0


sys.exit(main())
