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
uvx cookiecutter gh:michaeldunnpro/c_cookiecutter
```

Follow the prompts to customize your project. After the project is generated,
you can navigate to the project directory and run `make` to compile 
an executable, or `make clean` to clean up. Documentation for other commands 
is shown by invoking `make help`.
