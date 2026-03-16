def linear_rgb_to_srgb(r: float, g: float, b: float) -> tuple[int, int, int]:
    """Convert linear RGB color values to sRGB.

    Args:
        r: Red component in linear space (0.0-1.0)
        g: Green component in linear space (0.0-1.0)
        b: Blue component in linear space (0.0-1.0)

    Returns:
        Tuple of (r, g, b) where each component is 0-255
    """
    r_srgb = _gamma_correct(r)
    g_srgb = _gamma_correct(g)
    b_srgb = _gamma_correct(b)
    return round(r_srgb * 255), round(g_srgb * 255), round(b_srgb * 255)


def _gamma_correct(component: float) -> float:
    if component <= 0.0031308:
        return component * 12.92
    else:
        return 1.055 * (component ** (1.0 / 2.4)) - 0.055


def hsv_to_srgb(h: float, s: float, v: float) -> tuple[int, int, int]:
    """Convert HSV color values to sRGB.

    https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB

    Args:
        h: Hue in degrees (0-360)
        s: Saturation (0.0-1.0)
        v: Value (0.0-1.0)

    Returns:
        Tuple of (r, g, b) where each component is 0-255
    """

    # TODO: Write implementation here
    return 0, 0, 0
