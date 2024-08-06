# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/components/transform_relation.fbs".

# You can extend this class by creating a "TransformRelationExt" class in "transform_relation_ext.py".

from __future__ import annotations

from typing import Literal, Sequence, Union

import pyarrow as pa

from .._baseclasses import (
    BaseBatch,
    BaseExtensionType,
    ComponentBatchMixin,
)

__all__ = [
    "TransformRelation",
    "TransformRelationArrayLike",
    "TransformRelationBatch",
    "TransformRelationLike",
    "TransformRelationType",
]


from enum import Enum


class TransformRelation(Enum):
    """**Component**: Specifies relation a spatial transform describes."""

    ParentFromChild = 0
    """
    The transform describes how to transform into the parent entity's space.

    E.g. a translation of (0, 1, 0) with this [`components.TransformRelation`][rerun.components.TransformRelation] logged at `parent/child` means
    that from the point of view of `parent`, `parent/child` is translated 1 unit along `parent`'s Y axis.
    From perspective of `parent/child`, the `parent` entity is translated -1 unit along `parent/child`'s Y axis.
    """

    ChildFromParent = 1
    """
    The transform describes how to transform into the child entity's space.

    E.g. a translation of (0, 1, 0) with this [`components.TransformRelation`][rerun.components.TransformRelation] logged at `parent/child` means
    that from the point of view of `parent`, `parent/child` is translated -1 unit along `parent`'s Y axis.
    From perspective of `parent/child`, the `parent` entity is translated 1 unit along `parent/child`'s Y axis.
    """

    @classmethod
    def auto(cls, val: str | int | TransformRelation) -> TransformRelation:
        """Best-effort converter, including a case-insensitive string matcher."""
        if isinstance(val, TransformRelation):
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


TransformRelationLike = Union[
    TransformRelation, Literal["ChildFromParent", "ParentFromChild", "childfromparent", "parentfromchild"], int
]
TransformRelationArrayLike = Union[TransformRelationLike, Sequence[TransformRelationLike]]


class TransformRelationType(BaseExtensionType):
    _TYPE_NAME: str = "rerun.components.TransformRelation"

    def __init__(self) -> None:
        pa.ExtensionType.__init__(self, pa.uint8(), self._TYPE_NAME)


class TransformRelationBatch(BaseBatch[TransformRelationArrayLike], ComponentBatchMixin):
    _ARROW_TYPE = TransformRelationType()

    @staticmethod
    def _native_to_pa_array(data: TransformRelationArrayLike, data_type: pa.DataType) -> pa.Array:
        if isinstance(data, (TransformRelation, int, str)):
            data = [data]

        pa_data = [TransformRelation.auto(v).value if v is not None else None for v in data]  # type: ignore[redundant-expr]

        return pa.array(pa_data, type=data_type)
