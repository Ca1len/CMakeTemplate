cmake_minimum_required(VERSION 3.22)
project(test_cmake CXX)

find_package(cmake_template REQUIRED COMPONENTS Base Base2)

add_executable(test_package test.cpp)
target_include_directories(test_package PUBLIC ./include)
target_link_libraries(test_package PUBLIC cmake_template::Base)
