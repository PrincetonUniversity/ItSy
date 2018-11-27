# ---------------------------------------------------------------------------- #
# Dependencies
# Boost, z3, and Python
# ---------------------------------------------------------------------------- #
##
## Boost
##
set(Boost_USE_STATIC_LIBS OFF)
set(Boost_USE_MULTITHREADED ON)
set(Boost_USE_STATIC_RUNTIME OFF)

find_package(Boost 1.50 REQUIRED COMPONENTS python)

# This is needed if your Boost version is newer than your CMake version
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
message(STATUS "Python version: ${PYTHONLIBS_VERSION}")
if (PYTHONLIBS_FOUND)
  message(STATUS "PYTHON_LIBRARIES = ${PYTHON_LIBRARIES}")
  message(STATUS "PYTHON_INCLUDE_DIRS = ${PYTHON_INCLUDE_DIRS}")
endif()

if(NOT TARGET PythonLibs)
  add_library(PythonLibs IMPORTED INTERFACE)

  set_property(TARGET PythonLibs PROPERTY
    INTERFACE_INCLUDE_DIRECTORIES ${PYTHON_INCLUDE_DIRS}
  )

  set_property(TARGET PythonLibs PROPERTY
    INTERFACE_LINK_LIBRARIES ${PYTHON_LIBRARIES}
  )

endif()

##
## z3
##
find_package(Z3 REQUIRED)

# ---------------------------------------------------------------------------- #
# TARGET
# library target
# ---------------------------------------------------------------------------- #
add_library(${ILASYNTH_AST_LIB_NAME}
  ast/bitvec.cpp 
  ast/bool.cpp 
  ast/node.cpp 
  ast/choice.cpp 
  ast/bvinrange.cpp 
  ast/mem.cpp 
  ast/node.cpp
)

target_compile_features(${ILASYNTH_AST_LIB_NAME} PUBLIC cxx_std_11)

set_target_properties(${ILASYNTH_AST_LIB_NAME} PROPERTIES 
  POSITION_INDEPENDENT_CODE ON
)

#target_compile_options(${ILASYNTH_AST_LIB_NAME} PRIVATE 
#  -DBOOST_VARIANT_USE_RELAXED_GET_BY_DEFAULT
#)

target_link_libraries(${ILASYNTH_AST_LIB_NAME} PUBLIC Boost)
target_link_libraries(${ILASYNTH_AST_LIB_NAME} PUBLIC PythonLibs)
target_link_libraries(${ILASYNTH_AST_LIB_NAME} PUBLIC z3::z3)

##
## include paths
##
target_include_directories(${ILASYNTH_AST_LIB_NAME} 
  PUBLIC
    $<INSTALL_INTERFACE:${ILASYNTH_INCLUDE_INSTALL_DIR}>
    $<BUILD_INTERFACE:${ILASYNTH_INCLUDE_BUILD_DIR}>
)


# ---------------------------------------------------------------------------- #
# TARGET
# library target
# ---------------------------------------------------------------------------- #
add_library(${ILASYNTH_LIB_NAME} 
  abstraction.cpp 
  ast.cpp 
  cppsimgen.cpp 
  ext.cpp 
  logging.cpp 
  rewriter.cpp 
  smt.cpp 
  synthesizer.cpp 
  util.cpp 
  exception.cpp 
  imexport.cpp 
  memvalues.cpp 
  simplify.cpp 
  synrewriter.cpp 
  type.cpp 
  Unroller.cpp 
  EqvChecker.cpp
)

target_compile_features(${ILASYNTH_LIB_NAME} PUBLIC cxx_std_11)

set_target_properties(${ILASYNTH_LIB_NAME} PROPERTIES
  POSITION_INDEPENDENT_CODE ON
)

target_compile_options(${ILASYNTH_LIB_NAME} PRIVATE 
  -DBOOST_VARIANT_USE_RELAXED_GET_BY_DEFAULT
)

target_link_libraries(${ILASYNTH_LIB_NAME} PUBLIC Boost)
target_link_libraries(${ILASYNTH_LIB_NAME} PUBLIC PythonLibs)
target_link_libraries(${ILASYNTH_LIB_NAME} PUBLIC z3::z3)
target_link_libraries(${ILASYNTH_LIB_NAME} PUBLIC ${ILASYNTH_AST_LIB_NAME}) 

##
## include paths
##
target_include_directories(${ILASYNTH_LIB_NAME} 
  PUBLIC
    $<INSTALL_INTERFACE:${ILASYNTH_INCLUDE_INSTALL_DIR}>
    $<BUILD_INTERFACE:${ILASYNTH_INCLUDE_BUILD_DIR}>
)


# ---------------------------------------------------------------------------- #
# INSTALL
# install and export lib target
# ---------------------------------------------------------------------------- #
install(
  TARGETS ${ILASYNTH_AST_LIB_NAME} ${ILASYNTH_LIB_NAME}
  EXPORT ${ILASYNTH_TARGETS_EXPORT_NAME}
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
  RUNTIME DESTINATION bin
  INCLUDES DESTINATION ${ILASYNTH_INCLUDE_INSTALL_DIR}
)

##
## include directory
##
#configure_file(
#  ${PROJECT_SOURCE_DIR}/src/config.h.in
#  ${PROJECT_SOURCE_DIR}/include/ilang/config.h
#  @ONLY
#)

#install(
#  FILES ${ILANG_INCLUDE_BUILD_DIR}/ila-synth/cpp_api.h
#  DESTINATION ${ILANG_INCLUDE_INSTALL_DIR}
#  RENAME ila_synth.h
#)

install(
  DIRECTORY ${ILASYNTH_INCLUDE_BUILD_DIR}/ilasynth
  DESTINATION ${ILASYNTH_INCLUDE_INSTALL_DIR}
)


