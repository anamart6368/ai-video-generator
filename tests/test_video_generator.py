import pytest
from video_generator import VideoGenerator


def test_video_generator_init():
    vg = VideoGenerator(param1="value1", param2="value2")
    assert vg.param1 == "value1"
    assert vg.param2 == "value2"


def test_video_generation():
    vg = VideoGenerator(param1="value1", param2="value2")
    result = vg.generate_video()
    assert result is not None
    assert isinstance(result, str)  # Assuming the output is a file path or URL.


def test_video_generation_invalid_params():
    vg = VideoGenerator(param1=None, param2="value2")  # Invalid parameter
    with pytest.raises(ValueError):
        vg.generate_video()