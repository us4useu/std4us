from conan import ConanFile
from conan.tools.files import copy
import os

class std4usRecipe(ConanFile):
    name = "std4us"
    version = "0.0.1"
    package_type = "header-library"
    license = "MIT"
    url = "https://github.com/us4useu/std4us"
    description = "us4us C++ standard library extension"
    no_copy_source = True

    def export_sources(self):
        repo_root = os.path.join(self.recipe_folder, "..", "..", "..")
        
        source_include_dir = os.path.join(repo_root, "include")
        
        copy(self, pattern="*", 
             src=source_include_dir, 
             dst=os.path.join(self.export_sources_folder, "include"))

    def package(self):
        copy(self, pattern="*", 
             src=os.path.join(self.source_folder, "include"), 
             dst=os.path.join(self.package_folder, "include", "std4us"))

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.includedirs = ["include"]