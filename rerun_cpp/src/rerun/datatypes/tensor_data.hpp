// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/datatypes/tensor_data.fbs".

#pragma once

#include "../collection.hpp"
#include "../result.hpp"
#include "tensor_buffer.hpp"
#include "tensor_dimension.hpp"

#include <cstdint>
#include <memory>

namespace arrow {
    class Array;
    class DataType;
    class StructBuilder;
} // namespace arrow

namespace rerun::datatypes {
    /// **Datatype**: An N-dimensional array of numbers.
    ///
    /// The number of dimensions and their respective lengths is specified by the `shape` field.
    /// The dimensions are ordered from outermost to innermost. For example, in the common case of
    /// a 2D RGB Image, the shape would be `[height, width, channel]`.
    ///
    /// These dimensions are combined with an index to look up values from the `buffer` field,
    /// which stores a contiguous array of typed values.
    ///
    /// Note that the buffer may be encoded in a compressed format such as `jpeg` or
    /// in a format with downsampled chroma, such as NV12 or YUY2.
    /// For file formats, the shape is used as a hint, for chroma downsampled format
    /// the shape has to be the shape of the decoded image.
    struct TensorData {
        /// The shape of the tensor, including optional names for each dimension.
        rerun::Collection<rerun::datatypes::TensorDimension> shape;

        /// The content/data.
        rerun::datatypes::TensorBuffer buffer;

      public:
        // Extensions to generated type defined in 'tensor_data_ext.cpp'

        /// New tensor data from shape and tensor buffer.
        ///
        /// \param shape_ Shape of the tensor.
        /// \param buffer_ The tensor buffer containing the tensor's data.
        TensorData(
            Collection<rerun::datatypes::TensorDimension> shape_, datatypes::TensorBuffer buffer_
        )
            : shape(std::move(shape_)), buffer(std::move(buffer_)) {}

        /// New tensor data from dimensions and pointer to tensor data.
        ///
        /// Type must be one of the types supported by `rerun::datatypes::TensorData`.
        /// \param shape_ Shape of the tensor. Determines the number of elements expected to be in `data`.
        /// \param data Target of the pointer must outlive the archetype.
        template <typename TElement>
        explicit TensorData(Collection<datatypes::TensorDimension> shape_, const TElement* data)
            : shape(std::move(shape_)) {
            size_t num_elements = shape.empty() ? 0 : 1;
            for (const auto& dim : shape) {
                num_elements *= dim.size;
            }
            buffer = rerun::Collection<TElement>::borrow(data, num_elements);
        }

      public:
        TensorData() = default;
    };
} // namespace rerun::datatypes

namespace rerun {
    template <typename T>
    struct Loggable;

    /// \private
    template <>
    struct Loggable<datatypes::TensorData> {
        static constexpr const char Name[] = "rerun.datatypes.TensorData";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype();

        /// Serializes an array of `rerun::datatypes::TensorData` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const datatypes::TensorData* instances, size_t num_instances
        );

        /// Fills an arrow array builder with an array of this type.
        static rerun::Error fill_arrow_array_builder(
            arrow::StructBuilder* builder, const datatypes::TensorData* elements,
            size_t num_elements
        );
    };
} // namespace rerun
