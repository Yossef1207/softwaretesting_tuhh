import hashlib
from streamlink import Streamlink
from streamlink.plugins.twitcasting import TwitCasting
from unittest.mock import MagicMock


# Initialisation of plugin object 
def make_plugin(password=None):
    session = Streamlink()
    plugin = TwitCasting(session, "https://twitcasting.tv/testuser")
    plugin.match = {"channel": "testuser"}
    plugin.options = {"password": password} if password else {}
    return plugin

#es werden keine echten url benutzt und nur mocks durch MagicMock benutzt, da man sonst immer eine URL nutzen müsste, wo eine Person live wäre, was für das testen schlecht wäre



# Active Clause Coverage (ACC)
#testen vom 1 prädicat
#testen von 1 clausel
# movie muss false sein, sodass die exporession true wird


def test_acc_first_predicate_first_clause_true():
    plugin = make_plugin()
    plugin._api_query_streamserver = MagicMock(return_value=(
        None, {}, {}
    ))
    assert list(plugin._get_streams()) == []


# Active Clause Coverage (ACC)
#testen vom 1 prädicat
#testen von 1 clausel
# movie muss true sein, sodass die exporession false wird

def test_acc_first_predicate_first_clause_false():
    plugin = make_plugin()
    plugin._api_query_streamserver = MagicMock(return_value=(
        {"id": 123, "live": True}, {"streams": {"mytest": "https://twitcasting.tv/testuser"}}, None
    ))
    plugin._get_streams_websocket = MagicMock(return_value=iter(["ws_mytest", "https://twitcasting.tv/testuser"]))
    assert list(plugin._get_streams()) == ["ws_mytest", "https://twitcasting.tv/testuser"]


# Active Clause Coverage (ACC)
#testen vom 1 prädicat
#testen von 2 clausel
# id muss false sein, sodass die exporession true wird / live muss konstant sein


def test_acc_first_predicate_second_clause_true():
    plugin = make_plugin()
    plugin._api_query_streamserver = MagicMock(return_value=(
        {"id": None, "live": True}, {}, {}
    ))
    assert list(plugin._get_streams()) == []

# Active Clause Coverage (ACC)
#testen vom 1 prädicat
#testen von 2 clausel
# id muss true sein, sodass die exporession false wird / live muss konstant sein

def test_acc_first_predicate_second_clause_false():
    plugin = make_plugin()
    plugin._api_query_streamserver = MagicMock(return_value=(
        {"id": 123, "live": True}, {"streams": {"mytest": "https://twitcasting.tv/testuser"}}, None
    ))
    plugin._get_streams_websocket = MagicMock(return_value=iter(["ws_mytest", "https://twitcasting.tv/testuser"]))
    assert list(plugin._get_streams()) == ["ws_mytest", "https://twitcasting.tv/testuser"]

# Active Clause Coverage (ACC)
#testen vom 1 prädicat
#testen von 3 clausel
# live muss false sein, sodass die exporession true wird / id muss konstant sein

def test_acc_first_predicate_third_clause_true():
    plugin = make_plugin()
    plugin._api_query_streamserver = MagicMock(return_value=(
        {"id": 123, "live": False}, {}, {}
    ))
    assert list(plugin._get_streams()) == []

# Active Clause Coverage (ACC)
#testen vom 1 prädicat
#testen von 3 clausel
# live muss true sein, sodass die exporession false wird / id muss konstant sein

def test_acc_first_predicate_third_clause_false():
    plugin = make_plugin()
    plugin._api_query_streamserver = MagicMock(return_value=(
        {"id": 123, "live": True}, {"streams": {"mytest": "https://twitcasting.tv/testuser"}}, None
    ))
    plugin._get_streams_websocket = MagicMock(return_value=iter(["ws_mytest", "https://twitcasting.tv/testuser"]))
    assert list(plugin._get_streams()) == ["ws_mytest", "https://twitcasting.tv/testuser"]


# Active Clause Coverage (ACC)
#testen vom 2 prädicat
#testen von 1 clausel
# websocket muss false sein, damit die expression true wird / movie und hls muss konstant sein

def test_acc_second_predicate_first_clause_true():
    plugin = make_plugin()
    plugin._api_query_streamserver = MagicMock(return_value=(
        {"id": 1, "live": True}, None, None
    ))
    assert list(plugin._get_streams()) == []


# Active Clause Coverage (ACC)
#testen vom 2 prädicat
#testen von 1 clausel
# websocket muss true sein, damit die expression false wird / movie und hls muss konstant sein


def test_acc_second_predicate_first_clause_false():
    plugin = make_plugin()
    plugin._api_query_streamserver = MagicMock(return_value=(
        {"id": 1, "live": True}, {"streams": {"mytest": "https://twitcasting.tv/testuser"}}, None
    ))
    plugin._get_streams_websocket = MagicMock(return_value=iter(["ws_mytest", "https://twitcasting.tv/testuser"]))
    assert list(plugin._get_streams()) == ["ws_mytest", "https://twitcasting.tv/testuser"]


# Active Clause Coverage (ACC)
#testen vom 2 prädicat
#testen von 2 clausel
#hsl = false, sodass der ausdruck true wird / movie und websocket muss konstant sein


def test_acc_second_predicate_second_clause_true():
    plugin = make_plugin()
    plugin._api_query_streamserver = MagicMock(return_value=(
        {"id": 1, "live": True}, None, None  
    ))
    assert list(plugin._get_streams()) == []  


# Active Clause Coverage (ACC)
#testen vom 2 prädicat
#testen von 2 clausel
#hsl = true, sodass der ausdruck false wird / movie und websocket muss konstant sein


def test_acc_second_predicate_second_clause_false():
    plugin = make_plugin()
    plugin._api_query_streamserver = MagicMock(return_value=(
        {"id": 1, "live": True}, None, {"streams": {"mytest": "https://twitcasting.tv/testuser"}}
    ))
    plugin._get_streams_hls = MagicMock(return_value=iter(["hls_mytest"]))
    assert list(plugin._get_streams()) == ["hls_mytest"]



#### testen von nur einer clausel ############# nicht relevant


# def test_acc_password_clause_true():

#     plugin = make_plugin(password="test")
   
#     plugin._api_query_streamserver = MagicMock(return_value=(
#         {"id": 1, "live": True}, {"streams": {"mytest": "https://twitcasting.tv/testuser"}}, None
#     ))
    
#     plugin._get_streams_websocket = MagicMock(return_value=iter(["ws_mytest"]))
    
#     _ = list(plugin._get_streams())
#     # inspect params passed into _get_streams_websocket
#     called_params = plugin._get_streams_websocket.call_args[0][1]
#     expected_hash = hashlib.md5(b"test").hexdigest()
#     assert called_params == {"word": expected_hash}


# def test_acc_password_clause_false():
#     plugin = make_plugin()
#     plugin._api_query_streamserver = MagicMock(return_value=(
#         {"id": 1, "live": True}, {"streams": {"mytest": "https://twitcasting.tv/testuser"}}, None
#     ))
#     plugin._get_streams_websocket = MagicMock(return_value=iter(["ws_mytest"]))
#     _ = list(plugin._get_streams())
#     called_params = plugin._get_streams_websocket.call_args[0][1]
#     assert called_params == {}










# def test_acc_websocket_condition_true():

#     plugin = make_plugin()
    
#     plugin._api_query_streamserver = MagicMock(return_value=(
#         {"id": 1, "live": True},
#         {"streams": {"mytest": "https://twitcasting.tv/testuser"}},
#         None
#     ))
   
#     plugin._get_streams_websocket = MagicMock(return_value=iter(["ws_mytest"]))
#     result = list(plugin._get_streams())
#     assert result == ["ws_mytest"]


# def test_acc_websocket_condition_false():

#     plugin = make_plugin()
    
#     plugin._api_query_streamserver = MagicMock(return_value=(
#         {"id": 1, "live": True},
#         None,
#         {"streams": {"mytest": "https://twitcasting.tv/testuser"}}
#     ))
    
#     plugin._get_streams_hls = MagicMock(return_value=iter(["hls_mytest"]))
#     result = list(plugin._get_streams())
#     assert result == ["hls_mytest"]


# # --- ACC for “if hls:” ---

# def test_acc_hls_condition_true():

#     plugin = make_plugin()
   
#     plugin._api_query_streamserver = MagicMock(return_value=(
#         {"id": 1, "live": True},
#         None,
#         {"streams": {"mytest": "https://twitcasting.tv/testuser"}}
#     ))
#     plugin._get_streams_hls = MagicMock(return_value=iter(["hls_mytest"]))
#     result = list(plugin._get_streams())
#     assert result == ["hls_mytest"]


# def test_acc_hls_condition_false():

#     plugin = make_plugin()
  
#     plugin._api_query_streamserver = MagicMock(return_value=(
#         {"id": 1, "live": True},
#         {"streams": {"mytest": "https://twitcasting.tv/testuser"}},
#         None
#     ))
#     plugin._get_streams_websocket = MagicMock(return_value=iter(["ws_mytest"]))
#     result = list(plugin._get_streams())
#     assert result == ["ws_mytest"]
















