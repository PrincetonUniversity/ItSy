#ifndef _EXCEPTION_H_DEFINED_
#define _EXCEPTION_H_DEFINED_

#include <boost/exception/exception.hpp>
#include <boost/python.hpp>

namespace ilasynth {
/*
 * This is a wrapper class for all the exceptions
 * that will be thrown from the Python code.
 */
struct PyILAException : public boost::exception {
  PyObject* exception;
  std::string message;

  PyILAException(PyObject* ex, const std::string& msg)
      : exception(ex), message(msg) {}

  PyILAException(PyObject* ex, const char* msg) : exception(ex), message(msg) {}

  virtual ~PyILAException() throw();
};

void translateILAException(PyILAException const& ex);
} // namespace ilasynth
#endif // _EXCEPTION_H_DEFINED_
