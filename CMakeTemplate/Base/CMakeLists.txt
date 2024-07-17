set(component Base)
set(component_name ${PROJECT_NAME}_${component})

set(phony_source_path ${CMAKE_CURRENT_BINARY_DIR}/phony.cxx)

file(WRITE ${phony_source_path} "")

set(sources
  ${phony_source_path}
)

add_library(${component_name} ${sources})

add_library(${PROJECT_NAME}::${component} ALIAS ${component_name})

set_target_properties(
  ${component_name}
  PROPERTIES CXX_VISIBILITY_PRESET hidden
             VISIBILITY_INLINES_HIDDEN YES
             VERSION "${PROJECT_VERSION}"
             SOVERSION "${PROJECT_VERSION_MAJOR}"
             EXPORT_NAME ${component}
             OUTPUT_NAME ${component})

include(GenerateExportHeader)
generate_export_header(
  ${component_name}
  BASE_NAME
  ${PROJECT_NAME}
  EXPORT_FILE_NAME
  export/${PROJECT_NAME}/export.hpp
  CUSTOM_CONTENT_FROM_VARIABLE
  pragma_suppress_c4251)

target_include_directories(${component_name} PUBLIC
  "$<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/export/>"
  "$<INSTALL_INTERFACE:include/>"
)
