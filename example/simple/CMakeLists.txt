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
## z3
##
find_package(Z3 REQUIRED)

##
## Boost
##
find_package(Boost 1.50 REQUIRED COMPONENTS python)

if(NOT TARGET Boost)
  add_library(Boost IMPORTED INTERFACE)

  set_property(TARGET Boost PROPERTY
    INTERFACE_INCLUDE_DIRECTORIES ${Boost_INCLUDE_DIR}
  )

  set_property(TARGET Boost PROPERTY
    INTERFACE_LINK_LIBRARIES ${Boost_LIBRARIES}
  )

endif()

##
## Python
##
find_package(PythonLibs 2.7 REQUIRED)

if(NOT TARGET PythonLibs)
  add_library(PythonLibs IMPORTED INTERFACE)

  set_property(TARGET PythonLibs PROPERTY
    INTERFACE_INCLUDE_DIRECTORIES ${PYTHON_INCLUDE_DIRS}
  )

  set_property(TARGET PythonLibs PROPERTY
    INTERFACE_LINK_LIBRARIES ${PYTHON_LIBRARIES}
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
target_link_libraries(${MyTarget} z3::z3)
target_link_libraries(${MyTarget} Boost)
target_link_libraries(${MyTarget} PythonLibs)

