# Build: 07961b400f89d8b8a4c5a57dfc5082f9

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
