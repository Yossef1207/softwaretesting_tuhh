import re
import pytest
from hypothesis import given
from hypothesis.strategies import just
import sys


from streamlink_cli.utils.versioncheck import _parse_version



@given(just("0.0.0"))
def test_parse_version_01(version):
    assert _parse_version(version) == (0, 0, 0, 0)

@given(just("5.7.9"))
def test_parse_version_02(version):
    assert _parse_version(version) == (5, 7, 9, 0)

@given(just("1.3.3"))
def test_parse_version_03(version):
    assert _parse_version(version) == (1, 3, 3, 0)

@given(just("-9.-1.-3"))
def test_parse_version_04(version):
    try:
        _parse_version(version)
        assert False, "Expected ValueError"
    except ValueError:
        pass  # korrekt

@given(just("1.7.3+0"))
def test_parse_version_05(version):
    assert _parse_version(version) == (1, 7, 3, 0)

@given(just("9.1.3+5"))
def test_parse_version_06(version):
    assert _parse_version(version) == (9, 1, 3, 5)

@given(just("1.1.2-10"))
def test_parse_version_07(version):
    assert _parse_version(version) == (1,1,2,10)

@given(just("1.2.3"))
def test_parse_version_08(version):
    assert _parse_version(version) == (1, 2, 3, 0)

@given(just("1.2.3+4"))
def test_parse_version_09(version):
    assert _parse_version(version) == (1, 2, 3, 4)

@given(just("1.2"))
def test_parse_version_10(version):
    try:
        _parse_version(version)
        assert False, "Expected ValueError"
    except ValueError:
        pass  # korrekt

@given(just("1.9.44"))
def test_parse_version_11(version):
    assert _parse_version(version) == (1, 9, 44, 0)

@given(just("2.0.0"))
def test_parse_version_12(version):
    assert _parse_version(version) == (2, 0, 0, 0)

@given(just("0.0.7"))
def test_parse_version_13(version):
    assert _parse_version(version) == (0, 0, 7, 0)

@given(just("3.4.5+999"))
def test_parse_version_14(version):
    assert _parse_version(version) == (3, 4, 5, 999)

@given(just("3.4"))
def test_parse_version_15(version):
    try:
        _parse_version(version)
        assert False, "Expected ValueError"
    except ValueError:
        pass  # korrekt

@given(just("10.10.10"))
def test_parse_version_16(version):
    assert _parse_version(version) == (10, 10, 10, 0)

@given(just("1.9.44+1"))
def test_parse_version_17(version):
    assert _parse_version(version) == (1, 9, 44, 1)

@given(just("3.3.3-5"))
def test_parse_version_18(version):
    assert _parse_version(version) == (3, 3, 3, 5)

@given(just("01.02.03"))
def test_parse_version_19(version):
    assert _parse_version(version) == (1, 2, 3, 0)

@given(just("0.0.0+000"))
def test_parse_version_20(version):
    assert _parse_version(version) == (0, 0, 0, 0)

@given(just("999.999.999"))
def test_parse_version_21(version):
    assert _parse_version(version) == (999, 999, 999, 0)

@given(just("v.2.3"))
def test_parse_version_22(version):
    try:
        _parse_version(version)
        assert False, "Expected ValueError"
    except ValueError:
        pass  # korrekt

@given(just("1.l.3.5"))
def test_parse_version_23(version):
    try:
        _parse_version(version)
        assert False, "Expected ValueError"
    except ValueError:
        pass  # korrekt

@given(just("11.1.4"))
def test_parse_version_24(version):
    assert _parse_version(version) == (11,1,4,0)


@given(just("01.002.0003"))
def test_parse_version_25(version):
    assert _parse_version(version) == (1, 2, 3,0)

@given(just("0.0.0.0"))
def test_parse_version_26(version):
    assert _parse_version(version) == (0,0,0,0)

@given(just("x.b.q"))
def test_parse_version_27(version):
    try:
        _parse_version(version)
        assert False, "Expected ValueError"
    except ValueError:
        pass  # korrekt

@given(just("l.m"))
def test_parse_version_28(version):
    try:
        _parse_version(version)
        assert False, "Expected ValueError"
    except ValueError:
        pass  # korrekt

@given(just("-9.-34.0005"))
def test_parse_version_29(version):
    try:
        _parse_version(version)
        assert False, "Expected ValueError"
    except ValueError:
        pass  # korrekt

@given(just("-9.-34.0005+005"))
def test_parse_version_30(version):
    try:
        _parse_version(version)
        assert False, "Expected ValueError"
    except ValueError:
        pass  # korrekt