include_guard()

function (get_all_cmake_targets out_var current_dir)
  get_property(targets DIRECTORY ${current_dir} PROPERTY BUILDSYSTEM_TARGETS)
  get_property(subdirs DIRECTORY ${current_dir} PROPERTY SUBDIRECTORIES)

  foreach(subdir ${subdirs})
    get_all_cmake_targets(subdir_targets ${subdir})
    list(APPEND targets ${subdir_targets})
  endforeach()

  set(${out_var} ${targets} PARENT_SCOPE)
endfunction()

function (get_all_include_directories out_var targets)
  set(includes "")
  foreach(target ${targets})
    get_target_property(target_includes ${target} INTERFACE_INCLUDE_DIRECTORIES)
    list(APPEND includes ${target_includes})
  endforeach()

  set(${out_var} ${includes} PARENT_SCOPE)
endfunction()
