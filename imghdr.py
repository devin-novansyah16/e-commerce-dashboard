"""Minimal replacement for the standard-library `imghdr` module.

This implements a lightweight `what()` function sufficient for common image
types (jpeg, png, gif, bmp, webp, tiff, ico). It's intentionally small and
only used to satisfy packages that import `imghdr` on runtimes where the
stdlib module is missing (e.g. Python 3.13+ environments).
"""
from __future__ import annotations

from typing import Optional
import os


def _read_bytes(file, n=32):
    if file is None:
        return b""
    # file can be a path, bytes, or a file-like object
    if isinstance(file, (bytes, bytearray)):
        return bytes(file[:n])
    if isinstance(file, (str, os.PathLike)):
        with open(file, "rb") as f:
            return f.read(n)
    # file-like
    try:
        pos = None
        if hasattr(file, "seek") and hasattr(file, "tell"):
            pos = file.tell()
            file.seek(0)
        data = file.read(n)
        if pos is not None:
            file.seek(pos)
        return data or b""
    except Exception:
        return b""


def what(file: Optional[object], h: Optional[bytes] = None) -> Optional[str]:
    """Return a string describing the image type, or None if not recognized.

    Supports common types: 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'ico'.
    """
    header = h if h is not None else _read_bytes(file, 64)
    if not header:
        return None

    # JPEG
    if header.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    # PNG
    if header.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    # GIF
    if header.startswith(b"GIF87a") or header.startswith(b"GIF89a"):
        return "gif"
    # BMP
    if header.startswith(b"BM"):
        return "bmp"
    # TIFF
    if header.startswith(b"II*\x00") or header.startswith(b"MM\x00*"):
        return "tiff"
    # WEBP (RIFF ... WEBP)
    if header[0:4] == b"RIFF" and header[8:12] == b"WEBP":
        return "webp"
    # ICO
    if header.startswith(b"\x00\x00\x01\x00"):
        return "ico"

    return None


__all__ = ["what"]
