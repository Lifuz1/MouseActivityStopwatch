from Stopwatch_project.Stopwatch import ProStopWatch


def test_start_stopwatch(mocker):

    stopwatch = ProStopWatch(None)
    stopwatch.GUI_window = mocker.MagicMock()

    mock_after = mocker.patch.object(stopwatch.GUI_window, 'after')

    assert not stopwatch.is_running
    assert stopwatch.start_time is None
    assert stopwatch.elapsed_time == 0

    stopwatch.start_stopwatch()

    assert stopwatch.is_running
    assert stopwatch.start_time is not None
    assert stopwatch.start_button["text"] == "Stop Track"
    assert stopwatch.reset_button["state"] == "normal"

    mock_after.assert_called_once_with(100, stopwatch.update_time)

    stopwatch.start_stopwatch()

    assert not stopwatch.is_running
    assert stopwatch.start_button["text"] == "Start Track"

    stopwatch.reset_stopwatch()

    assert not stopwatch.is_running
    assert stopwatch.start_time is None
    assert stopwatch.elapsed_time == 0
    assert stopwatch.start_button["text"] == "Start Track"
    assert stopwatch.reset_button["state"] == "disabled"
