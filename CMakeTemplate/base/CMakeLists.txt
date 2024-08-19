set(component base)

set(phony_source_path ${CMAKE_CURRENT_BINARY_DIR}/phony.cxx)

file(WRITE ${phony_source_path} "")

set(sources ${phony_source_path})

add_library(${component} ${sources})

target_include_directories(
  ${component}
  PUBLIC "$<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/export/>"
         "$<INSTALL_INTERFACE:include/>")

set_target_properties(
  ${component}
  PROPERTIES CXX_VISIBILITY_PRESET hidden
             VISIBILITY_INLINES_HIDDEN YES
             VERSION "${PROJECT_VERSION}"
             SOVERSION "${PROJECT_VERSION_MAJOR}"
             EXPORT_NAME ${component}
             OUTPUT_NAME ${component})

include(GenerateExportHeader)
generate_export_header(
  ${component}
  BASE_NAME
  ${PROJECT_NAME}
  EXPORT_FILE_NAME
  export/${PROJECT_NAME}/export.hpp
  CUSTOM_CONTENT_FROM_VARIABLE
  pragma_suppress_c4251)


