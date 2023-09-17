from Stopwatch_project.Stopwatch import ProStopWatch


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
