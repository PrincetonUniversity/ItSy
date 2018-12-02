#include <ilasynth/exception.hpp>

namespace ilasynth {
// Exception translator.
void translateILAException(PyILAException const& ex) {
  PyErr_SetString(ex.exception, ex.message.c_str());
}

// Destructor.
PyILAException::~PyILAException() throw() {}
} // namespace ilasynth
