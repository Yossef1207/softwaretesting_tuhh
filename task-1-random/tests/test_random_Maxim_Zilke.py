from hypothesis import given
from hypothesis.strategies import floats, lists, integers, text
from hypothesis.strategies import just
import re
import string
import pytest
from hypothesis.strategies import text
import sys
from streamlink.options import Options



# 1: erhält zwei random alphabete mit mindestens einem unterstrich, welcher erstezt werden soll
@given(
    prefix=text(alphabet=string.ascii_lowercase + "_-"),
    suffix=text(alphabet=string.ascii_lowercase + "_-")
)
def test_normalize_key_contains_dash(prefix, suffix):
    input_str = prefix + "_" + suffix  # manuelle eingabe von "_", um in jedem test sicherzustellen, dass ein "_" vorhanden ist
    print(f"Generated input for prefix: {prefix}")  # Eingabe anzeigen
    print(f"Generated input for suffix: {suffix}")  # Eingabe anzeigen
    result = Options._normalize_key(input_str)

    # Es darf kein "_" vorkommen 
    assert "_" not in result


# 2: enthält keinen _ sodass der input string nicht verändert werden soll

@given(name=text(alphabet=string.ascii_letters, min_size=1))
def test_normalize_key_no_underscore_unchanged(name):
    # Wenn der Input keinen Unterstrich enthält, sollte die Ausgabe gleich bleiben
    result = Options._normalize_key(name)
    assert result == name


# 3. Test: Length remains the same
@given(text(alphabet=string.printable))
def test_length_preserved(name):
    normalized = Options._normalize_key(name)
    assert len(normalized) == len(name)



# 4. Test: execute normalised kex twize
@given(text(alphabet=string.ascii_lowercase + "_-"))
def test_double_execute(name):
    single = Options._normalize_key(name)
    double = Options._normalize_key(single)
    assert single == double


