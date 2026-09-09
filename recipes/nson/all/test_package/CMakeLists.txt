cmake_minimum_required(VERSION 3.15)
project(NsonTestPackage CXX)

find_package(nson CONFIG REQUIRED)

add_executable(example src/example.cpp)
target_link_libraries(example PRIVATE nson::nson)
target_compile_features(example PRIVATE cxx_std_23)
