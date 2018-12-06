
[![Build Status](https://travis-ci.org/PrincetonUniversity/ILA-Synthesis-Engine.svg?branch=master)](https://travis-ci.org/PrincetonUniversity/ILA-Synthesis-Engine)

## About 
This is an implementation of the templated-based synthesis of Instruction-Level Abstraction (ILA) based on [TCAD18](https://ieeexplore.ieee.org/document/8076885/). 

## License
The synthesis engine is licensed under MIT license. See [LICENSE](LICENSE) for details. 

## Dependencies 
[z3](https://github.com/Z3Prover/z3) 4.4.0 to 4.7.1.

[boost](https://www.boost.org) 1.50.0 or above.

## Installation
```bash
	cd <path/to/repo>
	bjam [-j4]
	export PYTHONPATH=$(pwd)/build:$PYTHONPATH
```

## Usage
``` python
	import ila
	abs = ila.Abstraction("test")
```

## People
