// lib.cc
// Synopsis: implementation of the library

#include <simple/lib.h>
#include <ilasynth/abstraction.hpp>
#include <iostream>

void Foo() {
  std::cout << "Hello from the lib." << std::endl;

  auto abs = ilasynth::Abstraction("abs");

  return;
}
