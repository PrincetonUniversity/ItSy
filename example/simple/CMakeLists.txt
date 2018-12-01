cmake_minimum_required(VERSION 3.8)

# ---------------------------------------------------------------------------- #
# PROJECT
# name version language
# ---------------------------------------------------------------------------- #
project(simple VERSION 1.0 LANGUAGES CXX)

# ---------------------------------------------------------------------------- #
# OPTION
# build configuration
# ---------------------------------------------------------------------------- #
option(MYPROJ_BUILD_TEST "Build unit tests if enabled."                      ON)

include(CMakeDependentOption)
cmake_dependent_option(MYPROJ_BUILD_COV 
  "Build with coverage if enabled."                                          ON
  "MYPROJ_BUILD_TEST AND CMAKE_BUILD_TYPE MATCHES Debug"                    OFF)

# ---------------------------------------------------------------------------- #
# VARIABLE
# alias and configurations
# ---------------------------------------------------------------------------- #
set(MyTarget ${PROJECT_NAME})

set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})

# ---------------------------------------------------------------------------- #
# External dependencies
# ---------------------------------------------------------------------------- #
##
## ilasynth
##
find_package(ilasynth REQUIRED)

##
## Python
##
# Imported target for Python is supported only for CMake >= 3.12
if(NOT TARGET Python::Python)

  message(STATUS "Imported target Python::Python not found.")

  add_library(Python::Python IMPORTED INTERFACE)

  set_property(TARGET Python::Python PROPERTY
    INTERFACE_INCLUDE_DIRECTORIES ${Python_INCLUDE_DIRS}
  )

  set_property(TARGET Python::Python PROPERTY
    INTERFACE_LINK_LIBRARIES ${Python_LIBRARIES}
  )

endif()


# ---------------------------------------------------------------------------- #
# TARGET
# executable
# ---------------------------------------------------------------------------- #
add_executable(${MyTarget} 
  app/main.cc
  src/lib.cc
)

target_include_directories(${MyTarget} PRIVATE include)

target_link_libraries(${MyTarget} ilasynth::ilasynth)

