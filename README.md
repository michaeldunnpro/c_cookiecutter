# Basic C Project Template
This is a basic C project template for use on UNIX-like systems that use the 
GNU Compiler (gcc). It is purposely as bare-bones as possible, and forgoes a 
meta-build system (e.g., CMake) in favor of simplicity.

The basic project structure consists of a directory with 'bin' and 
'src' directories. All '*.c' and '*.h' files should be placed directly
into the 'src' directory. Executables and linker files are output in
'bin' at compile time.

# Usage

To clone the template, run the following command in your terminal:

```bash
cookiecutter gh:michaeldunnpro/c_cookiecutter
```

Follow the prompts to customize your project. After the project is generated, navigate to the project directory and run:

```bash
make
```

To run the project, use:

```bash
make run
```

When writing code, place all source files ('.c' and '.h') in the 'src' directory. The Makefile will automatically compile all source files in 'src' and output the executable to the 'bin' directory.