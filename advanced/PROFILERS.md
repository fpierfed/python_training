# Python Profilers

## Introduction

Profilers are software programs that analyse the execution characteristics of other pieces of software (the ones we write).

Profilers are typically used to measure the memory usage of a program, its time complexity and/or the duration and call frequency of function calls.

Common profilers work either by instrumenting the code that they are going to measure (code profilers) or by attaching themselves to the running process and periodically probing its state (statistical profilers).


## Available Profilers

Python includes a code profiler ([cProfile](https://docs.python.org/3/library/profile.html#module-cProfile)) in its Standard Library. A number of tools exist to display the output of cProfile. One of the most popular ones is [snakeviz](https://jiffyclub.github.io/snakeviz/).

Other profilers are available as third-party packages. What follows is a curated list of the most common third-party profilers.


### Memory Profilers

* [Heapy](http://guppy-pe.sourceforge.net/#Heapy)
* [memory-profiler](https://pypi.org/project/memory-profiler/)
* [muppy](https://pythonhosted.org/Pympler/muppy.html)


### Object Graph Analysis

* [objgraph](https://mg.pov.lt/objgraph/)


### Line Profilers

* [line_profiler](https://github.com/rkern/line_profiler)


### All In One

* [vprof](https://github.com/nvdv/vprof)
* [Profiling](https://github.com/what-studio/profiling)


### Commercial

* [Intel VTune™ Amplifier](https://software.intel.com/en-us/vtune)