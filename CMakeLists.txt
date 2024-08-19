cmake_minimum_required(VERSION 3.28)

project(
  asd
  VERSION 0.1.0
  LANGUAGES CXX)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/)

add_subdirectory(${CMAKE_SOURCE_DIR}/CMakeTemplate/)

include(ComponentsUtils)

install_components(./CMakeTemplate/)

include(CMakePackageConfigHelpers)
configure_file("${CMAKE_SOURCE_DIR}/cmake/Config.cmake.in"
               "${CMAKE_BINARY_DIR}/${PROJECT_NAME}-config.cmake" @ONLY)
write_basic_package_version_file(
  "${CMAKE_BINARY_DIR}/${PROJECT_NAME}-config-version.cmake"
  VERSION ${CMAKE_PROJECT_VERSION}
  COMPATIBILITY AnyNewerVersion)
install(
  FILES "${CMAKE_BINARY_DIR}/${PROJECT_NAME}-config.cmake"
        "${CMAKE_BINARY_DIR}/${PROJECT_NAME}-config-version.cmake"
  DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}"
  COMPONENT ${PROJECT_NAME}_Development)

# CPack
include(InstallRequiredSystemLibraries)
set(CPACK_PACKAGE_NAME "${PROJECT_NAME}")
set(CPACK_GENERATOR "TGZ")
set(CPACK_SOURCE_GENERATOR "TGZ")
include(CPack)
