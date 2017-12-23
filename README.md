# ILA-Synthesis
Template-based synthesis for Instruction-Level Abstraction (ILA) and the corresponding Python API

## Building ILA synthesis tool

[![Build Status](https://travis-ci.org/PrincetonILA/ILA-Synthesis.svg?branch=master)](https://travis-ci.org/PrincetonILA/ILA-Synthesis)

### Dependencies 
[z3](https://github.com/Z3Prover/z3) 4.4.0 or above.

[boost](https://www.boost.org) 1.54.0 or above.

### Building with boost:

```bash
	cd path/to/repo/
	bjam [-j4]
```

### Building with cmake:

```bash
	cd path/to/repo/
	mkdir cbuild
	cd cbuild
	cmake ../ -L -DZ3_INCLUDE_DIR=/usr/include
```

### Set python path for python API:

```bash
	export PYTHONPATH=/path/to/repo/build/:$PYTHONPATH
```

## Reference
* __Template-based Parameterized Synthesis of Uniform Instruction-Level Abstractions for SoC Verification__.
  Pramod Subramanyan, Bo-Yuan Huang, Yakir Vizel, Aarti Gupta, and Sharad Malik.
  *in* IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), 2017.
  [[PDF](https://github.com/Bo-Yuan-Huang/ILA-Tools/blob/master/docs/publications/Template-based%20Parameterized%20Synthesis%20of%20Uniform%20Instruction-Level%20Abstractions%20for%20SoC%20Verification.pdf)]
