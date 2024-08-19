include_guard()

include(TargetsUtils)
include(InstallUtils)

function(get_components_directories components_directory outvar)
  get_property(
    ${outvar}
    DIRECTORY ${components_directory}
    PROPERTY SUBDIRECTORIES)
  set(${outvar}
      ${${outvar}}
      PARENT_SCOPE)
endfunction()

function(get_components_names components_directories outvar)
  foreach(subdir ${components_directories})
    cmake_path(GET subdir FILENAME name)
    list(APPEND ${outvar} ${name})
  endforeach()
  set(${outvar}
      ${${outvar}}
      PARENT_SCOPE)
endfunction()

function(install_components components_directory)
  get_components_directories(${components_directory} subdirs)
  get_components_names("${subdirs}" names)
  set(SUPPORTED_COMPONENTS "")

  foreach(name dir IN ZIP_LISTS names subdirs)
    message(STATUS "Found component: ${name}, ${dir}")
    get_all_cmake_targets(targets ${dir})
    component_install(${name} "${targets}")
    list(APPEND SUPPORTED_COMPONENTS ${name})
  endforeach()

endfunction()
