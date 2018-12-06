# ILA-Synthesis
The Python API for template-based synthesis for Instruction-Level Abstraction (ILA).

## Building ILA synthesis tool

[![Build Status](https://travis-ci.org/PrincetonUniversity/ILA-Synthesis-Engine.svg?branch=master)](https://travis-ci.org/PrincetonUniversity/ILA-Synthesis-Engine)

### Dependencies 
[z3](https://github.com/Z3Prover/z3) 4.4.0 or above.

[boost](https://www.boost.org) 1.54.0 or above.

### Building with boost:

```bash
	cd <path/to/repo>
	bjam [-j4]
```

### Building with cmake:

```bash
	cd <path/to/repo>
	mkdir cbuild
	cd cbuild
	cmake ../ -L -DZ3_INCLUDE_DIR=<directory/containing/z3/header>
```

### Set python path for python API:

```bash
	export PYTHONPATH=<path/to/repo/build>:$PYTHONPATH
```

## Reference
* __Template-based Parameterized Synthesis of Uniform Instruction-Level Abstractions for SoC Verification__.
  Pramod Subramanyan, Bo-Yuan Huang, Yakir Vizel, Aarti Gupta, and Sharad Malik.
  *in* IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), 2017.
  [[link](https://ieeexplore.ieee.org/document/8076885/)]
