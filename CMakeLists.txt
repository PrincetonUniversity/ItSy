cmake_minimum_required(VERSION 3.8)

if(${CMAKE_VERSION} VERSION_LESS 3.14)
  cmake_policy(VERSION ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION})
else()
  cmake_policy(VERSION 3.14)
endif()


# ---------------------------------------------------------------------------- #
# PROJECT
# name version language
# ---------------------------------------------------------------------------- #
project(ilasynth VERSION 1.0 
                 LANGUAGES CXX
)


# ---------------------------------------------------------------------------- #
# OPTION
# build configuration
# ---------------------------------------------------------------------------- #
option(ILASYNTH_EXPORT_PACKAGE "Export cmake package if enabled"            OFF)
option(ILASYNTH_BUILD_DOCS     "Build documentation if enabled"             OFF)
option(BUILD_SHARED_LIBS       "Build shared libraries"                     OFF)


# ---------------------------------------------------------------------------- #
# VARIABLE
# alias and configurations
# ---------------------------------------------------------------------------- #
set(ILASYNTH_TARGET_NAME                ${PROJECT_NAME})
set(ILASYNTH_CONFIG_INSTALL_DIR         "lib/cmake/${PROJECT_NAME}" CACHE INTERNAL "")
set(ILASYNTH_INCLUDE_INSTALL_DIR        "include")
set(ILASYNTH_INCLUDE_BUILD_DIR          "${PROJECT_SOURCE_DIR}/include")
set(ILASYNTH_TARGETS_EXPORT_NAME        "${PROJECT_NAME}Targets")
set(ILASYNTH_CMAKE_CONFIG_TEMPLATE      "cmake/config.cmake.in")
set(ILASYNTH_CMAKE_CONFIG_DIR           "${CMAKE_CURRENT_BINARY_DIR}")
set(ILASYNTH_CMAKE_PROJECT_TARGETS_FILE "${PROJECT_NAME}Targets.cmake")

set(ILASYNTH_CMAKE_VERSION_CONFIG_FILE
  "${ILASYNTH_CMAKE_CONFIG_DIR}/${PROJECT_NAME}ConfigVersion.cmake")

set(ILASYNTH_CMAKE_PROJECT_CONFIG_FILE
  "${ILASYNTH_CMAKE_CONFIG_DIR}/${PROJECT_NAME}Config.cmake")

set(BOOST_PY_COMP                       "python")

if(${BUILD_SHARED_LIBS})
  set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
  set(CMAKE_MACOSX_RPATH TRUE)
endif()


# ---------------------------------------------------------------------------- #
# External dependencies
# ---------------------------------------------------------------------------- #
##
## Make sure that custom modules can be found.
##
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})


# ---------------------------------------------------------------------------- #
# TARGET
# library target
# ---------------------------------------------------------------------------- #
set(ILASYNTH_LIB_NAME ${PROJECT_NAME})
set(ILASYNTH_AST_LIB_NAME ${ILASYNTH_LIB_NAME}Ast)
add_subdirectory(src)


# ---------------------------------------------------------------------------- #
# INSTALL
# project related
# ---------------------------------------------------------------------------- #
##
## forward version for find_package
##
include(CMakePackageConfigHelpers)
write_basic_package_version_file(
  ${ILASYNTH_CMAKE_VERSION_CONFIG_FILE} 
  COMPATIBILITY SameMajorVersion # AnyNewVersion
)

##
## cmake config
##
configure_file(
  ${ILASYNTH_CMAKE_CONFIG_TEMPLATE}
  ${ILASYNTH_CMAKE_PROJECT_CONFIG_FILE}
  @ONLY
)

install(
  FILES ${ILASYNTH_CMAKE_PROJECT_CONFIG_FILE} ${ILASYNTH_CMAKE_VERSION_CONFIG_FILE}
  DESTINATION ${ILASYNTH_CONFIG_INSTALL_DIR}
)

##
## project export
##
install(
  EXPORT ${ILASYNTH_TARGETS_EXPORT_NAME}
  DESTINATION ${ILASYNTH_CONFIG_INSTALL_DIR}
  NAMESPACE ${PROJECT_NAME}::
  FILE ${ILASYNTH_CMAKE_PROJECT_TARGETS_FILE}
)

export(
  TARGETS ${ILASYNTH_AST_LIB_NAME} ${ILASYNTH_LIB_NAME}
  NAMESPACE ${PROJECT_NAME}::
  FILE ${ILASYNTH_CMAKE_PROJECT_TARGETS_FILE}
)

if(${ILASYNTH_EXPORT_PACKAGE})
  export(PACKAGE ${PROJECT_NAME})
endif()


# ---------------------------------------------------------------------------- #
# UNINSTALL
# uninstall files listed in install_manifest.txt
# ---------------------------------------------------------------------------- #
if(NOT TARGET uninstall)
  configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/cmake_uninstall.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/cmake/cmake_uninstall.cmake"
    IMMEDIATE @ONLY
  )

  add_custom_target(uninstall
    COMMAND 
      ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/cmake/cmake_uninstall.cmake
  )

endif()


# ---------------------------------------------------------------------------- #
# Documents
# ---------------------------------------------------------------------------- #
if(${ILASYNTH_BUILD_DOCS})
  add_subdirectory(docs)
endif()

