# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/components/pixel_format.fbs".

# You can extend this class by creating a "PixelFormatExt" class in "pixel_format_ext.py".

from __future__ import annotations

from typing import Literal, Sequence, Union

import pyarrow as pa

from .._baseclasses import (
    BaseBatch,
    BaseExtensionType,
    ComponentBatchMixin,
)

__all__ = ["PixelFormat", "PixelFormatArrayLike", "PixelFormatBatch", "PixelFormatLike", "PixelFormatType"]


from enum import Enum


class PixelFormat(Enum):
    """
    **Component**: Specifieds a particular format of an [`archetypes.Image`][rerun.archetypes.Image].

    Most images can be described by a [`components.ColorModel`][rerun.components.ColorModel] and a [`components.ChannelDatatype`][rerun.components.ChannelDatatype],
    e.g. `RGB` and `U8` respectively.

    However, some image formats has chroma downsampling and/or
    use differing number of bits per channel, and that is what this [`components.PixelFormat`][rerun.components.PixelFormat] is for.

    All these formats support random access.

    For more compressed image formats, see [`archetypes.ImageEncoded`][rerun.archetypes.ImageEncoded].
    """

    NV12 = 0
    """
    NV12 (aka Y_UV12) is a YUV 4:2:0 chroma downsampled format with 12 bits per pixel and 8 bits per channel.

    First comes entire image in Y in one plane,
    followed by a plane with interleaved lines ordered as U0, V0, U1, V1, etc.
    """

    YUY2 = 1
    """
    YUY2 (aka YUYV or YUYV16), is a YUV 4:2:2 chroma downsampled format with 16 bits per pixel and 8 bits per channel.

    The order of the channels is Y0, U0, Y1, V0, all in the same plane.
    """

    @classmethod
    def auto(cls, val: str | int | PixelFormat) -> PixelFormat:
        """Best-effort converter, including a case-insensitive string matcher."""
        if isinstance(val, PixelFormat):
            return val
        if isinstance(val, int):
            return cls(val)
        try:
            return cls[val]
        except KeyError:
            val_lower = val.lower()
            for variant in cls:
                if variant.name.lower() == val_lower:
                    return variant
        raise ValueError(f"Cannot convert {val} to {cls.__name__}")

    def __str__(self) -> str:
        """Returns the variant name."""
        return self.name


PixelFormatLike = Union[PixelFormat, Literal["NV12", "YUY2", "nv12", "yuy2"], int]
PixelFormatArrayLike = Union[PixelFormatLike, Sequence[PixelFormatLike]]


class PixelFormatType(BaseExtensionType):
    _TYPE_NAME: str = "rerun.components.PixelFormat"

    def __init__(self) -> None:
        pa.ExtensionType.__init__(self, pa.uint8(), self._TYPE_NAME)


class PixelFormatBatch(BaseBatch[PixelFormatArrayLike], ComponentBatchMixin):
    _ARROW_TYPE = PixelFormatType()

    @staticmethod
    def _native_to_pa_array(data: PixelFormatArrayLike, data_type: pa.DataType) -> pa.Array:
        if isinstance(data, (PixelFormat, int, str)):
            data = [data]

        pa_data = [PixelFormat.auto(v).value if v is not None else None for v in data]  # type: ignore[redundant-expr]

        return pa.array(pa_data, type=data_type)
