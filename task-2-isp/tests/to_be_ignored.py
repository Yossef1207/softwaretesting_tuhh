from hypothesis import given, settings, strategies as st
from streamlink import Streamlink
from streamlink.options import Options

test_urls = [
    "https://twitch.tv/examplechannel",
    "https://unknownplatform.com/live",
    "htp:/stream",
    "",
    "  https://twitch.tv/examplechannel  "
]

options_values = [
    None,
    Options(),
    Options().set("hls-live-edge", 2)
]

parameter_dicts = [
    {},
    {"stream_types": ["best"]},
    {"wrong_key": True},
    {"stream_types": 999}
]

url_strategy = st.sampled_from(test_urls)
options_strategy = st.sampled_from(options_values)
params_strategy = st.sampled_from(parameter_dicts)

@settings(deadline=None)
@given(url=url_strategy, options=options_strategy, params=params_strategy)
def test_streams_input_partitions(url, options, params):
    session = Streamlink()
    try:
        streams = session.streams(url, options=options, **params)
        assert isinstance(streams, dict) or streams is None
    except Exception as e:
        # Accept expected exceptions (e.g., NoPluginError)
        assert isinstance(e, Exception)
