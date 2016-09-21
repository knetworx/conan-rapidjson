from conans import ConanFile
import os
from conans.tools import download
from conans.tools import unzip
from conans import CMake

class rapidjsonConan(ConanFile):
    name = "rapidjson"
    version = "1.1.0"
    ZIP_FOLDER_NAME = "rapidjson-%s" % version
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    url="http://github.com/knetworx/conan-rapidjson"
    license="https://github.com/miloyip/rapidjson/license.txt"
    exports="FindRapidjson.cmake"
    zip_name = "v%s.zip" % version
    unzipped_name = "rapidjson-%s" % version

    def source(self):
        url = "https://github.com/miloyip/rapidjson/archive/%s" % self.zip_name
        download(url, self.zip_name)
        unzip(self.zip_name)
        os.unlink(self.zip_name)

    def build(self):
        pass # rapidjson is header-only

    def package(self):
        # Copy findrapidjson script into project
        self.copy("FindRapidjson.cmake", ".", ".")

        # Copying headers
        self.copy(pattern="*.h", dst="./include", src="./%s/include" % self.unzipped_name, keep_path=True)

    def package_info(self):
        self.cpp_info.libs = ['rapidjson']
