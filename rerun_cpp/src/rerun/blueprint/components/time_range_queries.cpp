// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/blueprint/components/time_range_queries.fbs".

#include "time_range_queries.hpp"

#include "../../blueprint/datatypes/time_range_query.hpp"

#include <arrow/builder.h>
#include <arrow/type_fwd.h>

namespace rerun::blueprint::components {}

namespace rerun {
    const std::shared_ptr<arrow::DataType>&
        Loggable<blueprint::components::TimeRangeQueries>::arrow_datatype() {
        static const auto datatype = arrow::list(arrow::field(
            "item",
            Loggable<rerun::blueprint::datatypes::TimeRangeQuery>::arrow_datatype(),
            false
        ));
        return datatype;
    }

    Result<std::shared_ptr<arrow::Array>>
        Loggable<blueprint::components::TimeRangeQueries>::to_arrow(
            const blueprint::components::TimeRangeQueries* instances, size_t num_instances
        ) {
        // TODO(andreas): Allow configuring the memory pool.
        arrow::MemoryPool* pool = arrow::default_memory_pool();
        auto datatype = arrow_datatype();

        ARROW_ASSIGN_OR_RAISE(auto builder, arrow::MakeBuilder(datatype, pool))
        if (instances && num_instances > 0) {
            RR_RETURN_NOT_OK(
                Loggable<blueprint::components::TimeRangeQueries>::fill_arrow_array_builder(
                    static_cast<arrow::ListBuilder*>(builder.get()),
                    instances,
                    num_instances
                )
            );
        }
        std::shared_ptr<arrow::Array> array;
        ARROW_RETURN_NOT_OK(builder->Finish(&array));
        return array;
    }

    rerun::Error Loggable<blueprint::components::TimeRangeQueries>::fill_arrow_array_builder(
        arrow::ListBuilder* builder, const blueprint::components::TimeRangeQueries* elements,
        size_t num_elements
    ) {
        if (builder == nullptr) {
            return rerun::Error(ErrorCode::UnexpectedNullArgument, "Passed array builder is null.");
        }
        if (elements == nullptr) {
            return rerun::Error(
                ErrorCode::UnexpectedNullArgument,
                "Cannot serialize null pointer to arrow array."
            );
        }

        auto value_builder = static_cast<arrow::StructBuilder*>(builder->value_builder());
        ARROW_RETURN_NOT_OK(builder->Reserve(static_cast<int64_t>(num_elements)));
        ARROW_RETURN_NOT_OK(value_builder->Reserve(static_cast<int64_t>(num_elements * 2)));

        for (size_t elem_idx = 0; elem_idx < num_elements; elem_idx += 1) {
            const auto& element = elements[elem_idx];
            ARROW_RETURN_NOT_OK(builder->Append());
            if (element.queries.data()) {
                RR_RETURN_NOT_OK(
                    Loggable<rerun::blueprint::datatypes::TimeRangeQuery>::fill_arrow_array_builder(
                        value_builder,
                        element.queries.data(),
                        element.queries.size()
                    )
                );
            }
        }

        return Error::ok();
    }
} // namespace rerun
