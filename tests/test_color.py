"""
:Authors: cykooz
:Date: 12.03.2026
"""

import pytest
from lessons.color import hsv_to_srgb, linear_rgb_to_srgb


@pytest.mark.parametrize(
    'r, g, b, expected',
    [
        (0.0, 0.0, 0.0, (0, 0, 0)),  # Black
        (1.0, 1.0, 1.0, (255, 255, 255)),  # White
        (0.5, 0.5, 0.5, (188, 188, 188)),  # Gray
        (1.0, 0.0, 0.0, (255, 0, 0)),  # Red
        (0.0, 1.0, 0.0, (0, 255, 0)),  # Green
        (0.0, 0.0, 1.0, (0, 0, 255)),  # Blue
        # Below the gamma threshold (0.003 * 12.92 * 255 ≈ 9.88)
        (0.003, 0.003, 0.003, (10, 10, 10)),
        # Above the gamma threshold (1.055 * 0.004^(1/2.4) - 0.055) * 255 ≈ 13.46 -> 13
        (0.004, 0.004, 0.004, (13, 13, 13)),
    ],
)
def test_linear_rgb_to_srgb(r, g, b, expected):
    result = linear_rgb_to_srgb(r, g, b)
    assert result == expected


@pytest.mark.parametrize(
    'h, s, v, expected',
    [
        (0, 0, 0, (0, 0, 0)),  # Black
        (0, 0, 1, (255, 255, 255)),  # White
        (0, 0, 0.5, (188, 188, 188)),  # Gray (around middle of sRGB range)
        (0, 1, 1, (255, 0, 0)),  # Red
        (60, 1, 1, (255, 255, 0)),  # Yellow
        (120, 1, 1, (0, 255, 0)),  # Green
        (180, 1, 1, (0, 255, 255)),  # Cyan
        (240, 1, 1, (0, 0, 255)),  # Blue
        (300, 1, 1, (255, 0, 255)),  # Magenta
        (360, 1, 1, (255, 0, 0)),  # Red (360 is same as 0)
        (420, 1, 1, (255, 255, 0)),  # Yellow (420 % 360 = 60)
        (0, 0.5, 1, (255, 188, 188)),  # Light Red
        (0, 1, 0.5, (188, 0, 0)),  # Dark Red
    ],
)
def test_hsv_to_srgb(h, s, v, expected):
    result = hsv_to_srgb(h, s, v)
    assert result == expected
