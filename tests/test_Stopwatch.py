from Stopwatch_project.Stopwatch import ProStopWatch
import pytest
import time
import openpyxl


def test_change_threshold(mocker):

    stopwatch = ProStopWatch(None)
    mocker.patch('tkinter.simpledialog.askinteger', return_value=None)

    stopwatch.change_threshold()
    assert stopwatch.threshold_time == 60
    assert stopwatch.threshold_label.cget('text') == "Threshold: 60 s"

    mocker.patch('tkinter.simpledialog.askinteger', return_value=10)

    stopwatch.change_threshold()

    assert stopwatch.threshold_time == 10
    assert stopwatch.threshold_label.cget('text') == "Threshold: 10 s"


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


def test_update_time(mocker):

    stopwatch = ProStopWatch(None)
    stopwatch.GUI_window = mocker.MagicMock()

    stopwatch.is_running = True
    stopwatch.start_time = time.time() - 1800
    stopwatch.elapsed_time = 1800

    stopwatch.update_time()

    assert stopwatch.elapsed_time == pytest.approx(1800)


@pytest.mark.parametrize("elapsed_time, expected_output", [(7265, "02:01:05")])  # elapsed time is passed in seconds
def test_save_time(tmpdir, monkeypatch, elapsed_time, expected_output):

    stopwatch = ProStopWatch(None)

    monkeypatch.setattr('tkinter.filedialog.asksaveasfilename', lambda **kwargs: tmpdir.join('test.xlsx'))
    stopwatch.elapsed_time = elapsed_time
    stopwatch.save_time()

    file_path = tmpdir.join('test.xlsx')
    assert file_path.exists()

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    cell_value = sheet.cell(row=1, column=2).value
    assert cell_value == expected_output
