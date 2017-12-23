# ILA-Synthesis
Template-based synthesis for Instruction-Level Abstraction (ILA) and the corresponding Python API

## Building ILA synthesis tool

[![Build Status](https://travis-ci.org/PrincetonILA/ILA-Synthesis.svg?branch=master)](https://travis-ci.org/PrincetonILA/ILA-Synthesis)

#### z3 
Building ILA synthesis tool requires [z3](https://github.com/Z3Prover/z3) 4.4.0 or above.

#### boost
Building ILA synthesis tool requires [boost](https://www.boost.org) 1.60.0 or above.

### Building with boost:

```bash
	cd path/to/synthesis/libcpp/
	bjam [-j4]
```

### Building with cmake:

```bash
	cd path/to/synthesis/libcpp/
	mkdir cbuild
	cd cbuild
	cmake ../ -L -DZ3_INCLUDE_DIR=/usr/include
```

#### Set python path for python API:

```bash
	export PYTHONPATH=/path/to/repo/build/:$PYTHONPATH
```
