[![Build Status](https://travis-ci.org/knetworx/conan-rapidjson.svg)](https://travis-ci.org/knetworx/conan-rapidjson)


# conan-rapidjson

[Conan.io](https://conan.io) package for rapidjson library

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py
    
## Upload packages to server

    $ conan upload rapidjson/1.1.0@knetworx/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install rapidjson/1.1.0@knetworx/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    rapidjson/1.1.0@knetworx/testing

    [options]
    rapidjson:shared=true # false
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
