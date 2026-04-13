from __future__ import annotations


def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None if injective."""
    # === TODO ===
    seen = {} # stores values seen so far
    for key, value in mapping.items():
        if value in seen:   # if we've seen this value before
            return (seen[value], key) # return both keys
        seen[value] = key # remember this value
    return None # no duplicates found, so it's injective
    # === END TODO ===


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None if surjective."""
    # === TODO ===
    for element in target:
        if element not in mapping.values(): # not in range
            return element # found one!
    return None # all target elements are in the range, so it's surjective
    # === END TODO ===


def my_floor(x: float) -> int:
    """Return floor(x) without using math.floor."""
    # === TODO ===
    n = int(x) # truncates towards zero
    if x < n: # negative with decimal, need to go lower
        return n - 1
    return n    
    # === END TODO ===


def my_ceil(x: float) -> int:
    """Return ceil(x) without using math.ceil."""
    # === TODO ===
    n = int(x) # truncates towards zero
    if x > n: # positive with decimal, need to go higher
        return n + 1
    return n 
    # === END TODO ===
