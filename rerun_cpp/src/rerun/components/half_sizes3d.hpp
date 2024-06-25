// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/components/half_sizes3d.fbs".

#pragma once

#include "../datatypes/vec3d.hpp"
#include "../result.hpp"

#include <array>
#include <cstdint>
#include <memory>

namespace rerun::components {
    /// **Component**: Half-size (radius) of a 3D box.
    ///
    /// Measured in its local coordinate system.
    ///
    /// The box extends both in negative and positive direction along each axis.
    /// Negative sizes indicate that the box is flipped along the respective axis, but this has no effect on how it is displayed.
    struct HalfSizes3D {
        rerun::datatypes::Vec3D xyz;

      public:
        // Extensions to generated type defined in 'half_sizes3d_ext.cpp'

        /// Construct HalfSizes3D from x/y/z values.
        HalfSizes3D(float x, float y, float z) : xyz{x, y, z} {}

        float x() const {
            return xyz.x();
        }

        float y() const {
            return xyz.y();
        }

        float z() const {
            return xyz.z();
        }

      public:
        HalfSizes3D() = default;

        HalfSizes3D(rerun::datatypes::Vec3D xyz_) : xyz(xyz_) {}

        HalfSizes3D& operator=(rerun::datatypes::Vec3D xyz_) {
            xyz = xyz_;
            return *this;
        }

        HalfSizes3D(std::array<float, 3> xyz_) : xyz(xyz_) {}

        HalfSizes3D& operator=(std::array<float, 3> xyz_) {
            xyz = xyz_;
            return *this;
        }

        /// Cast to the underlying Vec3D datatype
        operator rerun::datatypes::Vec3D() const {
            return xyz;
        }
    };
} // namespace rerun::components

namespace rerun {
    static_assert(sizeof(rerun::datatypes::Vec3D) == sizeof(components::HalfSizes3D));

    /// \private
    template <>
    struct Loggable<components::HalfSizes3D> {
        static constexpr const char Name[] = "rerun.components.HalfSizes3D";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype() {
            return Loggable<rerun::datatypes::Vec3D>::arrow_datatype();
        }

        /// Serializes an array of `rerun::components::HalfSizes3D` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const components::HalfSizes3D* instances, size_t num_instances
        ) {
            return Loggable<rerun::datatypes::Vec3D>::to_arrow(&instances->xyz, num_instances);
        }
    };
} // namespace rerun
