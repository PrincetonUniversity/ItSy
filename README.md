[![Build Status](https://semaphoreci.com/api/v1/bo-yuan-huang/ila-synthesis-python/branches/master/shields_badge.svg)](https://semaphoreci.com/bo-yuan-huang/ila-synthesis-python)
[![Build Status](https://travis-ci.org/PrincetonUniversity/ILA-Synthesis-Engine.svg?branch=master)](https://travis-ci.org/PrincetonUniversity/ILA-Synthesis-Engine)
[![Build status](https://ci.appveyor.com/api/projects/status/6wigyt506lel7kep/branch/master?svg=true)](https://ci.appveyor.com/project/Bo-Yuan-Huang/ila-synthesis-engine/branch/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e36f95e9ce45432ba515a996728fe6e5)](https://www.codacy.com/app/Bo-Yuan-Huang/ILA-Synthesis-Engine?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=PrincetonUniversity/ILA-Synthesis-Engine&amp;utm_campaign=Badge_Grade)
[![Language grade: C/C++](https://img.shields.io/lgtm/grade/cpp/g/PrincetonUniversity/ILA-Synthesis-Engine.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/PrincetonUniversity/ILA-Synthesis-Engine/context:cpp)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/PrincetonUniversity/ILA-Synthesis-Engine.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/PrincetonUniversity/ILA-Synthesis-Engine/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/PrincetonUniversity/ILA-Synthesis-Engine.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/PrincetonUniversity/ILA-Synthesis-Engine/alerts/)

- [Dependencies](#dependencies)
- [Building](#building)
  - [Boost for Python API](#boost-for-python-api)
  - [CMake for C++ Projects](#cmake-for-cpp-projects)
- [Python API](#python-api)
- [CMake Integration](#cmake-integration)
  - [External](#external)
  - [Embedded](#embedded)
  - [Supporting Both](#supporting-both)

## About 

This is an implementation of the templated-based synthesis of Instruction-Level Abstraction (ILA) based on [TCAD18](https://ieeexplore.ieee.org/document/8076885/). 

## License

The synthesis engine is licensed under MIT license. See [LICENSE](LICENSE) for details. 

## Dependencies 

- [z3](https://github.com/Z3Prover/z3) 4.4.0 or above.
- [boost](https://www.boost.org) 1.50.0 or above.

## Building

The ILA synthesis engine support build using `Boost bjam` and `CMake`.
Currently, unit tests are available in the Boost build only. 

### Boost for Python API

``` bash
cd /root/of/this/repo
bjam -j$(nproc)

```

### CMake for Cpp Projects

``` bash
cd /root/of/this/repo
mkdir -p build
cd build
cmake ..
make -j$(nproc)
```

## Python API

You need to first export the library. 

``` bash
# bash
export PYTHONPATH=$(pwd)/build:$PYTHONPATH
```

``` python
# Python 
import ila
abs = ila.Abstraction("test")
```

## CMake Integration
You can use the `ilasynth::ilasynth` interface target in CMake. 
This target populates the appropriate usage requirements for include directories, linked libraries, and compile features. 

``` c++
#include <ilasynth/abstraction.hpp>

void foo () {
  auto m = ilasynth::Abstraction("new_abstraction");
}
```

### External

To use the library from a CMake project, you can locate it directly with `find_package()` and use the namespaced imported target from the generated package configuration:

``` cmake
# CMakeLists.txt
find_package(ilasynth REQUIRED)
...
add_library(my_proj ...)
...
target_link_libraries(my_proj PRIVATE ilasynth::ilasynth)
```

### Embedded

It also supports embedded build, but is not recommended due to its size. 
To embed the library directly into an existing CMake project, place the entire source tree in a subdirectory and call `add_subdirectory()` in your `CMakeLists.txt` file:

``` cmake 
add_subdirectory(ilasynth)
...
add_library(my_proj ...)
...
target_link_libraries(my_proj PRIVATE ilasynth::ilasynth)
```

### Supporting Both

To allow your project to support either an externally installed or an embedded library, you can use the following pattern:

``` cmake
# Top level CMakeLists.txt
project(MY_PROJ)
...
option(MY_PROJ_USE_EXTERNAL_ILANG "Use an external library" OFF)
...
add_subdirectory(externals)
...
add_library(my_proj ...)
...
target_link_libraries(my_proj PRIVATE ilasynth::ilasynth)
```

``` cmake
# externals/CMakeLists.txt
...
if(MY_PROJ_USE_EXTERNAL_ILANG)
  find_package(ilasynth REQUIRED)
else()
  add_subdirectory(ilasynth)
endif()
...
```

`externals/ilasynth` is then a complete copy of this source tree, if enabled.
