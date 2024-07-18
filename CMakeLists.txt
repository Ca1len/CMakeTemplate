cmake_minimum_required(VERSION 3.28)

file(READ "./VERSION" project_version)
string(STRIP ${project_version} project_version)

project(
  CMakeTemplate
  VERSION ${project_version}
  LANGUAGES CXX
)

list(APPEND CMAKE_MODULE_PATH ./cmake/)

add_subdirectory(./CMakeTemplate/)

# Run at end of top-level CMakeLists
include(TargetsUtils)
get_all_cmake_targets(project_targets ${CMAKE_CURRENT_LIST_DIR})
message(STATUS "Project Targets: ${project_targets}")
get_all_include_directories(project_includes "${project_targets}")
message(STATUS "Project Includes: ${project_includes}")

# Install
include(GNUInstallDirs)
install(
  TARGETS ${project_targets}
  EXPORT ${PROJECT_NAME}Targets
  RUNTIME # Following options apply to runtime artifacts.
          COMPONENT Runtime
  LIBRARY # Following options apply to library artifacts.
          COMPONENT Runtime NAMELINK_COMPONENT Development
  ARCHIVE # Following options apply to archive artifacts.
          COMPONENT Development
          DESTINATION "${CMAKE_INSTALL_LIBDIR}"
          FILE_SET HEADERS # Following options apply to file set HEADERS.
          COMPONENT Development)
install(
  DIRECTORY
  ${project_includes}
  DESTINATION
  "${CMAKE_INSTALL_INCLUDEDIR}"
)
include(InstallUtils)
export_targets()
install_configs()

# CPack
include(InstallRequiredSystemLibraries)
set(CPACK_PACKAGE_NAME "${PROJECT_NAME}")
set(CPACK_GENERATOR "TGZ")
set(CPACK_SOURCE_GENERATOR "TGZ")
include(CPack)
