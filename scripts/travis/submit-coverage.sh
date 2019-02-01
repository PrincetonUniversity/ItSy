#!/bin/bash
set -ev
lcov --directory $1 --capture --output-file ./coverage.info
lcov --remove ./coverage.info '*/test/*' '/usr/*' --output-file ./coverage.info
lcov --list ./coverage.info
coveralls-lcov ./coverage.info 

