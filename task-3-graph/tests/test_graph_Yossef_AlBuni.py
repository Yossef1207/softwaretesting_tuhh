################# - test open_subprocess() - ############################
import pytest
from unittest.mock import patch, MagicMock, PropertyMock
from pathlib import Path
from streamlink_cli.output.player import PlayerOutput

@patch("streamlink_cli.output.player.subprocess.Popen")
def test_open_subprocess_exits_early(mock_popen):
    mock_proc = MagicMock()
    mock_popen.return_value = mock_proc

    po = PlayerOutput(Path("echo"))
    type(po).running = PropertyMock(return_value=False)  # ← Prozess nicht laufend

    with pytest.raises(OSError, match="Process exited prematurely"):
        po._open_subprocess(["echo", "test"])

@patch("streamlink_cli.output.player.subprocess.Popen")
def test_open_subprocess_namedpipe(mock_popen):
    mock_proc = MagicMock()
    mock_popen.return_value = mock_proc

    pipe = MagicMock()

    po = PlayerOutput(Path("echo"))
    type(po).running = PropertyMock(return_value=True)
    po.namedpipe = pipe

    po._open_subprocess(["echo", "test"])

    pipe.open.assert_called_once()

@patch("streamlink_cli.output.player.subprocess.Popen")
def test_open_subprocess_http(mock_popen):
    mock_proc = MagicMock()
    mock_popen.return_value = mock_proc

    http = MagicMock()

    po = PlayerOutput(Path("echo"))
    type(po).running = PropertyMock(return_value=True)
    po.http = http
    po.namedpipe = None

    po._open_subprocess(["echo", "test"])

    http.accept_connection.assert_called_once()
    http.open.assert_called_once()


################# - test close() - ############################

import pytest
from unittest.mock import Mock, patch
from streamlink_cli.output.player import PlayerOutput
from pathlib import Path
p = PlayerOutput(Path("dummy/path"))

@pytest.fixture
def dummy_player():
    return Mock(
        stdin=Mock(),
        terminate=Mock(),
        wait=Mock(),
        poll=Mock(return_value=None),
        returncode=None,
        kill=Mock()
    )

def test_close_namedpipe_only(dummy_player):
    p = PlayerOutput(Path("dummy/path"))
    p.namedpipe = Mock()
    p.http = None
    p.filename = True
    p.record = None
    p.kill = False
    p.player = dummy_player

    p._close()
    p.namedpipe.close.assert_called_once()

def test_close_http_only(dummy_player):
    p = PlayerOutput(Path("dummy/path"))
    p.namedpipe = None
    p.http = Mock()
    p.filename = True
    p.record = None
    p.kill = False
    p.player = dummy_player

    p._close()
    p.http.shutdown.assert_called_once()

def test_close_no_filename(dummy_player):
    p = PlayerOutput(Path("dummy/path"))
    p.namedpipe = None
    p.http = None
    p.filename = False
    p.record = None
    p.kill = False
    p.player = dummy_player

    p._close()
    p.player.stdin.close.assert_called_once()

def test_close_with_record(dummy_player):
    p = PlayerOutput(Path("dummy/path"))
    p.namedpipe = None
    p.http = None
    p.filename = True
    p.record = Mock()
    p.kill = False
    p.player = dummy_player

    p._close()
    p.record.close.assert_called_once()

@patch("streamlink_cli.output.player.is_win32", False)
@patch("streamlink_cli.output.player.sleep", lambda x: None)
def test_close_with_kill(dummy_player):
    dummy_player.poll.side_effect = [None, None, 0]
    dummy_player.returncode = None

    p = PlayerOutput(Path("dummy/path"))
    p.namedpipe = None
    p.http = None
    p.filename = True
    p.record = None
    p.kill = True
    p.player = dummy_player

    p._close()
    dummy_player.terminate.assert_called_once()
    dummy_player.kill.assert_called_once()
    dummy_player.wait.assert_called_once()

@patch("streamlink_cli.output.player.is_win32", False)
@patch("streamlink_cli.output.player.sleep", lambda x: None)
def test_close_kill_branch_returncode_none():
    from types import SimpleNamespace

    dummy_player = Mock()
    dummy_player.stdin = Mock()
    dummy_player.terminate = Mock()
    dummy_player.wait = Mock()
    dummy_player.kill = Mock()

    # poll() gibt immer None zurück → Schleife läuft bis Timeout
    dummy_player.poll.side_effect = lambda: None

    # returncode wird wie echtes Attribut behandelt
    dummy_player._returncode = None
    type(dummy_player).returncode = property(lambda self: self._returncode)

    p = PlayerOutput(Path("dummy/path"))
    p.namedpipe = None
    p.http = None
    p.filename = True
    p.record = None
    p.kill = True
    p.player = dummy_player
    p.PLAYER_TERMINATE_TIMEOUT = 0.5  # klein halten für Test

    p._close()

    dummy_player.terminate.assert_called_once()
    dummy_player.kill.assert_called_once()
    dummy_player.wait.assert_called_once()



################# - test get_namedpipe() - ############################

import pytest
from unittest.mock import patch, Mock
from pathlib import Path
from streamlink_cli.output.player import PlayerArgsVLC

@pytest.fixture
def namedpipe_mock():
    mock = Mock()
    mock.path = "testpipe"
    return mock

@patch("streamlink_cli.output.player.is_win32", True)
def test_get_namedpipe_windows(namedpipe_mock):
    player = PlayerArgsVLC(Path("dummy/path"))
    result = player.get_namedpipe(namedpipe_mock)
    assert result == "stream://\\testpipe"

@patch("streamlink_cli.output.player.is_win32", False)
def test_get_namedpipe_non_windows(namedpipe_mock):
    player = PlayerArgsVLC(Path("dummy/path"))

    with patch.object(
        PlayerArgsVLC.__bases__[0],  # PlayerArgs
        "get_namedpipe",
        return_value="super_called"
    ) as super_method:
        result = player.get_namedpipe(namedpipe_mock)
        super_method.assert_called_once_with(namedpipe_mock)
        assert result == "super_called"
