from hypothesis import given, strategies as st
from streamlink.plugin.plugin import iterate_streams

@given(
    st.lists(
        st.tuples(
            st.text(min_size=1, max_size=10),
            st.one_of(
                st.text(),  # single stream
                st.lists(st.text(), min_size=1, max_size=3)  # list of streams
            )
        ),
        min_size=0, max_size=5
    )
)
def test_iterate_streams_random(streams):
    # Should yield all streams, flattening lists
    result = list(iterate_streams(streams))
    # Check that result is a list of tuples (name, stream)
    for name, stream in result:
        assert isinstance(name, str)