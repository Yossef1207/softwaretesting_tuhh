import pytest
from types import SimpleNamespace
from streamlink_cli.output.player import PlayerOutput

class DummyWriter:
    def __init__(self):
        self.written = []

    def write(self, data):
        self.written.append(data)

def make_output(record=None, namedpipe=None, http=None):
    out = object.__new__(PlayerOutput)
    out.record = record
    out.namedpipe = namedpipe
    out.http = http
    out.player = SimpleNamespace(stdin=DummyWriter())
    return out

def test_write_to_record_only():
    test = DummyWriter()
    output = make_output(record=test)
    output._write("test-data")
    assert test.written == ["test-data"]

def test_write_to_namedpipe_only():
    test = DummyWriter()
    output = make_output(namedpipe=test)
    output._write("Maxim")
    assert test.written == ["Maxim"]

def test_write_to_http_only():
    test = DummyWriter()
    output = make_output(http=test)
    output._write("Zilke")
    assert test.written == ["Zilke"]

def test_write_to_stdin_only():
    output = make_output()
    output._write("final")
    assert output.player.stdin.written == ["final"]




