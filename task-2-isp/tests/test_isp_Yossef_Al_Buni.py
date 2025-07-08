import pytest
from streamlink import Streamlink
from streamlink.exceptions import NoPluginError
from streamlink.options import Options

@pytest.fixture
def session():
    return Streamlink()

def test_supported_plugin_valid_url(session):
    url = "https://twitch.tv/examplechannel"
    streams = session.streams(url)
    assert isinstance(streams, dict)

def test_supported_plugin_with_options(session):
    url = "https://twitch.tv/examplechannel"
    options = Options().set("hls-live-edge", 2)
    streams = session.streams(url, options=options)
    assert isinstance(streams, dict)

def test_supported_plugin_with_valid_params(session):
    url = "https://twitch.tv/examplechannel"
    params = {"stream_types": ["best"]}
    streams = session.streams(url, **params)
    assert isinstance(streams, dict)

def test_supported_plugin_with_invalid_params(session):
    url = "https://twitch.tv/examplechannel"
    params = {"wrong_key": True}
    with pytest.raises(Exception):
        session.streams(url, **params)

def test_unsupported_plugin_url(session):
    url = "https://unknownplatform.com/live"
    with pytest.raises(NoPluginError):
        session.streams(url)

def test_malformed_url(session):
    url = "htp:/stream"
    with pytest.raises(NoPluginError):
        session.streams(url)

def test_empty_url(session):
    url = ""
    with pytest.raises(NoPluginError):
        session.streams(url)

def test_url_with_whitespace(session):
    url = "  https://twitch.tv/examplechannel  "
    streams = session.streams(url.strip())
    assert isinstance(streams, dict)
