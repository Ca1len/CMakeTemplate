set(component component1)

set(sources ./src/component1.cpp)

add_library(${component} ${sources})

target_link_libraries(${component} PUBLIC base)

target_include_directories(
  ${component}
  PUBLIC "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include/>"
         "$<INSTALL_INTERFACE:include/>")

add_executable(${component}_app ./app/component1.cpp)
target_link_libraries(${component}_app ${component})
