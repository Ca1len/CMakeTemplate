cmake_minimum_required(VERSION 3.28)

file(READ "./VERSION" project_version)
string(STRIP ${project_version} project_version)

project(
  CMakeTemplate
  VERSION ${project_version}
  LANGUAGES CXX)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/)

find_package(fmt REQUIRED)

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
