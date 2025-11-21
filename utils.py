# utils.py
from datetime import datetime
from dateutil import parser

def parse_date(s):
    if not s:
        return None
    try:
        dt = parser.parse(s)
        return dt.isoformat()
    except Exception:
        raise ValueError("Invalid date format. Use YYYY-MM-DD or other ISO-parsable format.")

def pretty_row(d):
    return ", ".join(f"{k}: {v}" for k, v in d.items())