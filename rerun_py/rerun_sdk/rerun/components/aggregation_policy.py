# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/components/aggregation_policy.fbs".

# You can extend this class by creating a "AggregationPolicyExt" class in "aggregation_policy_ext.py".

from __future__ import annotations

from typing import Literal, Sequence, Union

import pyarrow as pa

from .._baseclasses import (
    BaseBatch,
    BaseExtensionType,
    ComponentBatchMixin,
)

__all__ = [
    "AggregationPolicy",
    "AggregationPolicyArrayLike",
    "AggregationPolicyBatch",
    "AggregationPolicyLike",
    "AggregationPolicyType",
]


from enum import Enum


class AggregationPolicy(Enum):
    """
    **Component**: Policy for aggregation of multiple scalar plot values.

    This is used for lines in plots when the X axis distance of individual points goes below a single pixel,
    i.e. a single pixel covers more than one tick worth of data. It can greatly improve performance
    (and readability) in such situations as it prevents overdraw.
    """

    Off = 0
    """No aggregation."""

    Average = 1
    """Average all points in the range together."""

    Max = 2
    """Keep only the maximum values in the range."""

    Min = 3
    """Keep only the minimum values in the range."""

    MinMax = 4
    """
    Keep both the minimum and maximum values in the range.

    This will yield two aggregated points instead of one, effectively creating a vertical line.
    """

    MinMaxAverage = 5
    """Find both the minimum and maximum values in the range, then use the average of those."""

    @classmethod
    def auto(cls, val: str | int | AggregationPolicy) -> AggregationPolicy:
        """Best-effort converter, including a case-insensitive string matcher."""
        if isinstance(val, AggregationPolicy):
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


AggregationPolicyLike = Union[
    AggregationPolicy,
    Literal[
        "Average",
        "Max",
        "Min",
        "MinMax",
        "MinMaxAverage",
        "Off",
        "average",
        "max",
        "min",
        "minmax",
        "minmaxaverage",
        "off",
    ],
    int,
]
AggregationPolicyArrayLike = Union[AggregationPolicyLike, Sequence[AggregationPolicyLike]]


class AggregationPolicyType(BaseExtensionType):
    _TYPE_NAME: str = "rerun.components.AggregationPolicy"

    def __init__(self) -> None:
        pa.ExtensionType.__init__(self, pa.uint8(), self._TYPE_NAME)


class AggregationPolicyBatch(BaseBatch[AggregationPolicyArrayLike], ComponentBatchMixin):
    _ARROW_TYPE = AggregationPolicyType()

    @staticmethod
    def _native_to_pa_array(data: AggregationPolicyArrayLike, data_type: pa.DataType) -> pa.Array:
        if isinstance(data, (AggregationPolicy, int, str)):
            data = [data]

        pa_data = [AggregationPolicy.auto(v).value if v is not None else None for v in data]  # type: ignore[redundant-expr]

        return pa.array(pa_data, type=data_type)
