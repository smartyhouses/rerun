# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/blueprint/components/view_fit.fbs".

# You can extend this class by creating a "ViewFitExt" class in "view_fit_ext.py".

from __future__ import annotations

from typing import Literal, Sequence, Union

import pyarrow as pa

from ..._baseclasses import (
    BaseBatch,
    BaseExtensionType,
    ComponentBatchMixin,
)

__all__ = ["ViewFit", "ViewFitArrayLike", "ViewFitBatch", "ViewFitLike", "ViewFitType"]


from enum import Enum


class ViewFit(Enum):
    """**Component**: Determines whether an image or texture should be scaled to fit the viewport."""

    Original = 0
    """No scaling, pixel size will match the image's width/height dimensions in pixels."""

    Fill = 1
    """Scale the image for the largest possible fit in the view's container."""

    FillKeepAspectRatio = 2
    """Scale the image for the largest possible fit in the view's container, but keep the original aspect ratio."""

    @classmethod
    def auto(cls, val: str | int | ViewFit) -> ViewFit:
        """Best-effort converter, including a case-insensitive string matcher."""
        if isinstance(val, ViewFit):
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


ViewFitLike = Union[
    ViewFit, Literal["Fill", "FillKeepAspectRatio", "Original", "fill", "fillkeepaspectratio", "original"], int
]
ViewFitArrayLike = Union[ViewFitLike, Sequence[ViewFitLike]]


class ViewFitType(BaseExtensionType):
    _TYPE_NAME: str = "rerun.blueprint.components.ViewFit"

    def __init__(self) -> None:
        pa.ExtensionType.__init__(self, pa.uint8(), self._TYPE_NAME)


class ViewFitBatch(BaseBatch[ViewFitArrayLike], ComponentBatchMixin):
    _ARROW_TYPE = ViewFitType()

    @staticmethod
    def _native_to_pa_array(data: ViewFitArrayLike, data_type: pa.DataType) -> pa.Array:
        if isinstance(data, (ViewFit, int, str)):
            data = [data]

        pa_data = [ViewFit.auto(v).value if v is not None else None for v in data]  # type: ignore[redundant-expr]

        return pa.array(pa_data, type=data_type)
