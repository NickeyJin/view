cmake_minimum_required(VERSION 3.25)
project(robot_actions LANGUAGES CXX)

add_executable(demo
    src/main.cpp
    src/action.cpp
    src/robot.cpp
    include/action.h
    include/robot.h
)
target_include_directories(demo PRIVATE include)
target_compile_features(demo PRIVATE cxx_std_20)