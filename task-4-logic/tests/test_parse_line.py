from streamlink.stream.hls.m3u8 import M3U8Parser
from unittest.mock import Mock


# Covers: Predicate Coverage (PC) – Predicate is True
def test_parse_line_predicate_true():
    parser = M3U8Parser()
    line = "#"
    parser.split_tag = lambda l: ("", None)
    parser.parse_line(line)

# Covers: Predicate Coverage (PC) – Predicate is False
def test_parse_line_predicate_false():
    parser = M3U8Parser()
    line = "#EXTINF:10,"
    parser.split_tag = lambda l: ("EXTINF", "10")
    handler_mock = Mock()
    parser._TAGS = {"EXTINF": handler_mock}
    parser.parse_line(line)
    handler_mock.assert_called_once_with(parser, "10")