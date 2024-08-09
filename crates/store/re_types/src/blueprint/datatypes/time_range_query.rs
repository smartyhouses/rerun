// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/rust/api.rs
// Based on "crates/store/re_types/definitions/rerun/blueprint/datatypes/time_range_query.fbs".

#![allow(unused_imports)]
#![allow(unused_parens)]
#![allow(clippy::clone_on_copy)]
#![allow(clippy::cloned_instead_of_copied)]
#![allow(clippy::map_flatten)]
#![allow(clippy::needless_question_mark)]
#![allow(clippy::new_without_default)]
#![allow(clippy::redundant_closure)]
#![allow(clippy::too_many_arguments)]
#![allow(clippy::too_many_lines)]

use ::re_types_core::external::arrow2;
use ::re_types_core::ComponentName;
use ::re_types_core::SerializationResult;
use ::re_types_core::{ComponentBatch, MaybeOwnedComponentBatch};
use ::re_types_core::{DeserializationError, DeserializationResult};

/// **Datatype**: Time range query configuration for a specific timeline.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct TimeRangeQuery {
    /// Name of the timeline this applies to.
    pub timeline: crate::datatypes::Utf8,

    /// Beginning of the time range.
    pub start: crate::datatypes::TimeInt,

    /// End of the time range (inclusive).
    pub end: crate::datatypes::TimeInt,
}

impl ::re_types_core::SizeBytes for TimeRangeQuery {
    #[inline]
    fn heap_size_bytes(&self) -> u64 {
        self.timeline.heap_size_bytes() + self.start.heap_size_bytes() + self.end.heap_size_bytes()
    }

    #[inline]
    fn is_pod() -> bool {
        <crate::datatypes::Utf8>::is_pod()
            && <crate::datatypes::TimeInt>::is_pod()
            && <crate::datatypes::TimeInt>::is_pod()
    }
}

::re_types_core::macros::impl_into_cow!(TimeRangeQuery);

impl ::re_types_core::Loggable for TimeRangeQuery {
    type Name = ::re_types_core::DatatypeName;

    #[inline]
    fn name() -> Self::Name {
        "rerun.blueprint.datatypes.TimeRangeQuery".into()
    }

    #[inline]
    fn arrow_datatype() -> arrow2::datatypes::DataType {
        #![allow(clippy::wildcard_imports)]
        use arrow2::datatypes::*;
        DataType::Struct(std::sync::Arc::new(vec![
            Field::new(
                "timeline",
                <crate::datatypes::Utf8>::arrow_datatype(),
                false,
            ),
            Field::new(
                "start",
                <crate::datatypes::TimeInt>::arrow_datatype(),
                false,
            ),
            Field::new("end", <crate::datatypes::TimeInt>::arrow_datatype(), false),
        ]))
    }

    fn to_arrow_opt<'a>(
        data: impl IntoIterator<Item = Option<impl Into<::std::borrow::Cow<'a, Self>>>>,
    ) -> SerializationResult<Box<dyn arrow2::array::Array>>
    where
        Self: Clone + 'a,
    {
        #![allow(clippy::wildcard_imports)]
        use ::re_types_core::{Loggable as _, ResultExt as _};
        use arrow2::{array::*, datatypes::*};
        Ok({
            let (somes, data): (Vec<_>, Vec<_>) = data
                .into_iter()
                .map(|datum| {
                    let datum: Option<::std::borrow::Cow<'a, Self>> = datum.map(Into::into);
                    (datum.is_some(), datum)
                })
                .unzip();
            let bitmap: Option<arrow2::bitmap::Bitmap> = {
                let any_nones = somes.iter().any(|some| !*some);
                any_nones.then(|| somes.into())
            };
            StructArray::new(
                Self::arrow_datatype(),
                vec![
                    {
                        let (somes, timeline): (Vec<_>, Vec<_>) = data
                            .iter()
                            .map(|datum| {
                                let datum = datum.as_ref().map(|datum| datum.timeline.clone());
                                (datum.is_some(), datum)
                            })
                            .unzip();
                        let timeline_bitmap: Option<arrow2::bitmap::Bitmap> = {
                            let any_nones = somes.iter().any(|some| !*some);
                            any_nones.then(|| somes.into())
                        };
                        {
                            let offsets = arrow2::offset::Offsets::<i32>::try_from_lengths(
                                timeline.iter().map(|opt| {
                                    opt.as_ref().map(|datum| datum.0.len()).unwrap_or_default()
                                }),
                            )?
                            .into();
                            let inner_data: arrow2::buffer::Buffer<u8> = timeline
                                .into_iter()
                                .flatten()
                                .flat_map(|datum| datum.0 .0)
                                .collect();

                            #[allow(unsafe_code, clippy::undocumented_unsafe_blocks)]
                            unsafe {
                                Utf8Array::<i32>::new_unchecked(
                                    DataType::Utf8,
                                    offsets,
                                    inner_data,
                                    timeline_bitmap,
                                )
                            }
                            .boxed()
                        }
                    },
                    {
                        let (somes, start): (Vec<_>, Vec<_>) = data
                            .iter()
                            .map(|datum| {
                                let datum = datum.as_ref().map(|datum| datum.start.clone());
                                (datum.is_some(), datum)
                            })
                            .unzip();
                        let start_bitmap: Option<arrow2::bitmap::Bitmap> = {
                            let any_nones = somes.iter().any(|some| !*some);
                            any_nones.then(|| somes.into())
                        };
                        PrimitiveArray::new(
                            DataType::Int64,
                            start
                                .into_iter()
                                .map(|datum| datum.map(|datum| datum.0).unwrap_or_default())
                                .collect(),
                            start_bitmap,
                        )
                        .boxed()
                    },
                    {
                        let (somes, end): (Vec<_>, Vec<_>) = data
                            .iter()
                            .map(|datum| {
                                let datum = datum.as_ref().map(|datum| datum.end.clone());
                                (datum.is_some(), datum)
                            })
                            .unzip();
                        let end_bitmap: Option<arrow2::bitmap::Bitmap> = {
                            let any_nones = somes.iter().any(|some| !*some);
                            any_nones.then(|| somes.into())
                        };
                        PrimitiveArray::new(
                            DataType::Int64,
                            end.into_iter()
                                .map(|datum| datum.map(|datum| datum.0).unwrap_or_default())
                                .collect(),
                            end_bitmap,
                        )
                        .boxed()
                    },
                ],
                bitmap,
            )
            .boxed()
        })
    }

    fn from_arrow_opt(
        arrow_data: &dyn arrow2::array::Array,
    ) -> DeserializationResult<Vec<Option<Self>>>
    where
        Self: Sized,
    {
        #![allow(clippy::wildcard_imports)]
        use ::re_types_core::{Loggable as _, ResultExt as _};
        use arrow2::{array::*, buffer::*, datatypes::*};
        Ok({
            let arrow_data = arrow_data
                .as_any()
                .downcast_ref::<arrow2::array::StructArray>()
                .ok_or_else(|| {
                    let expected = Self::arrow_datatype();
                    let actual = arrow_data.data_type().clone();
                    DeserializationError::datatype_mismatch(expected, actual)
                })
                .with_context("rerun.blueprint.datatypes.TimeRangeQuery")?;
            if arrow_data.is_empty() {
                Vec::new()
            } else {
                let (arrow_data_fields, arrow_data_arrays) =
                    (arrow_data.fields(), arrow_data.values());
                let arrays_by_name: ::std::collections::HashMap<_, _> = arrow_data_fields
                    .iter()
                    .map(|field| field.name.as_str())
                    .zip(arrow_data_arrays)
                    .collect();
                let timeline = {
                    if !arrays_by_name.contains_key("timeline") {
                        return Err(DeserializationError::missing_struct_field(
                            Self::arrow_datatype(),
                            "timeline",
                        ))
                        .with_context("rerun.blueprint.datatypes.TimeRangeQuery");
                    }
                    let arrow_data = &**arrays_by_name["timeline"];
                    {
                        let arrow_data = arrow_data
                            .as_any()
                            .downcast_ref::<arrow2::array::Utf8Array<i32>>()
                            .ok_or_else(|| {
                                let expected = DataType::Utf8;
                                let actual = arrow_data.data_type().clone();
                                DeserializationError::datatype_mismatch(expected, actual)
                            })
                            .with_context("rerun.blueprint.datatypes.TimeRangeQuery#timeline")?;
                        let arrow_data_buf = arrow_data.values();
                        let offsets = arrow_data.offsets();
                        arrow2::bitmap::utils::ZipValidity::new_with_validity(
                            offsets.iter().zip(offsets.lengths()),
                            arrow_data.validity(),
                        )
                        .map(|elem| {
                            elem.map(|(start, len)| {
                                let start = *start as usize;
                                let end = start + len;
                                if end > arrow_data_buf.len() {
                                    return Err(DeserializationError::offset_slice_oob(
                                        (start, end),
                                        arrow_data_buf.len(),
                                    ));
                                }

                                #[allow(unsafe_code, clippy::undocumented_unsafe_blocks)]
                                let data =
                                    unsafe { arrow_data_buf.clone().sliced_unchecked(start, len) };
                                Ok(data)
                            })
                            .transpose()
                        })
                        .map(|res_or_opt| {
                            res_or_opt.map(|res_or_opt| {
                                res_or_opt.map(|v| {
                                    crate::datatypes::Utf8(::re_types_core::ArrowString(v))
                                })
                            })
                        })
                        .collect::<DeserializationResult<Vec<Option<_>>>>()
                        .with_context("rerun.blueprint.datatypes.TimeRangeQuery#timeline")?
                        .into_iter()
                    }
                };
                let start = {
                    if !arrays_by_name.contains_key("start") {
                        return Err(DeserializationError::missing_struct_field(
                            Self::arrow_datatype(),
                            "start",
                        ))
                        .with_context("rerun.blueprint.datatypes.TimeRangeQuery");
                    }
                    let arrow_data = &**arrays_by_name["start"];
                    arrow_data
                        .as_any()
                        .downcast_ref::<Int64Array>()
                        .ok_or_else(|| {
                            let expected = DataType::Int64;
                            let actual = arrow_data.data_type().clone();
                            DeserializationError::datatype_mismatch(expected, actual)
                        })
                        .with_context("rerun.blueprint.datatypes.TimeRangeQuery#start")?
                        .into_iter()
                        .map(|opt| opt.copied())
                        .map(|res_or_opt| res_or_opt.map(crate::datatypes::TimeInt))
                };
                let end = {
                    if !arrays_by_name.contains_key("end") {
                        return Err(DeserializationError::missing_struct_field(
                            Self::arrow_datatype(),
                            "end",
                        ))
                        .with_context("rerun.blueprint.datatypes.TimeRangeQuery");
                    }
                    let arrow_data = &**arrays_by_name["end"];
                    arrow_data
                        .as_any()
                        .downcast_ref::<Int64Array>()
                        .ok_or_else(|| {
                            let expected = DataType::Int64;
                            let actual = arrow_data.data_type().clone();
                            DeserializationError::datatype_mismatch(expected, actual)
                        })
                        .with_context("rerun.blueprint.datatypes.TimeRangeQuery#end")?
                        .into_iter()
                        .map(|opt| opt.copied())
                        .map(|res_or_opt| res_or_opt.map(crate::datatypes::TimeInt))
                };
                arrow2::bitmap::utils::ZipValidity::new_with_validity(
                    ::itertools::izip!(timeline, start, end),
                    arrow_data.validity(),
                )
                .map(|opt| {
                    opt.map(|(timeline, start, end)| {
                        Ok(Self {
                            timeline: timeline
                                .ok_or_else(DeserializationError::missing_data)
                                .with_context(
                                    "rerun.blueprint.datatypes.TimeRangeQuery#timeline",
                                )?,
                            start: start
                                .ok_or_else(DeserializationError::missing_data)
                                .with_context("rerun.blueprint.datatypes.TimeRangeQuery#start")?,
                            end: end
                                .ok_or_else(DeserializationError::missing_data)
                                .with_context("rerun.blueprint.datatypes.TimeRangeQuery#end")?,
                        })
                    })
                    .transpose()
                })
                .collect::<DeserializationResult<Vec<_>>>()
                .with_context("rerun.blueprint.datatypes.TimeRangeQuery")?
            }
        })
    }
}
