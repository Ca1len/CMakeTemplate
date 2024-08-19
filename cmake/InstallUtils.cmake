include_guard()

include(TargetsUtils)

function(component_install component_name component_targets)
  include(GNUInstallDirs)

  install(
    TARGETS ${component_targets}
    EXPORT ${component_name}-targets
    RUNTIME #
            COMPONENT ${PROJECT_NAME}_Runtime
    LIBRARY #
            COMPONENT ${PROJECT_NAME}_Runtime
            NAMELINK_COMPONENT ${PROJECT_NAME}_Development
    ARCHIVE #
            COMPONENT ${PROJECT_NAME}_Development
    INCLUDES #
    DESTINATION
      "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}/${PROJECT_NAME}_${component_name}-${CMAKE_PROJECT_VERSION}"
  )

  export(
    EXPORT ${component_name}-targets
    FILE "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}/${PROJECT_NAME}_${component_name}-${CMAKE_PROJECT_VERSION}/${PROJECT_NAME}-${component_name}-targets.cmake"
    NAMESPACE ${PROJECT_NAME}::)

  install(
    EXPORT ${component_name}-targets
    FILE "${PROJECT_NAME}-${component_name}-targets.cmake"
    NAMESPACE ${PROJECT_NAME}::
    DESTINATION
      "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}/${PROJECT_NAME}_${component_name}-${CMAKE_PROJECT_VERSION}"
    COMPONENT ${component_name})

  include(CMakePackageConfigHelpers)
  configure_file(
    "${CMAKE_SOURCE_DIR}/cmake/component-config.cmake.in"
    "${CMAKE_BINARY_DIR}/${PROJECT_NAME}/${PROJECT_NAME}_${component_name}-${CMAKE_PROJECT_VERSION}/${PROJECT_NAME}-${component_name}-config.cmake"
    @ONLY)
  write_basic_package_version_file(
    "${CMAKE_BINARY_DIR}/${PROJECT_NAME}/${PROJECT_NAME}_${component_name}-${CMAKE_PROJECT_VERSION}/${PROJECT_NAME}-${component_name}-config-version.cmake"
    VERSION ${CMAKE_PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion)

  install(
    FILES
      "${CMAKE_BINARY_DIR}/${PROJECT_NAME}/${PROJECT_NAME}_${component_name}-${CMAKE_PROJECT_VERSION}/${PROJECT_NAME}-${component_name}-config.cmake"
      "${CMAKE_BINARY_DIR}/${PROJECT_NAME}/${PROJECT_NAME}_${component_name}-${CMAKE_PROJECT_VERSION}/${PROJECT_NAME}-${component_name}-config-version.cmake"
    DESTINATION
      "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}/${PROJECT_NAME}_${component_name}-${CMAKE_PROJECT_VERSION}"
    COMPONENT ${PROJECT_NAME}_Development)

  get_all_include_directories(component_includes "${component_targets}")
  install(
    DIRECTORY ${component_includes}
    DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}"
    COMPONENT ${PROJECT_NAME}_Development)
endfunction()
