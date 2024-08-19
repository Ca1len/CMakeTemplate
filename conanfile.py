from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
import shutil
import pathlib


class CMakeTemplate(ConanFile):
    name = "cmake_template"
    version = "0.0.0"

    license = "Pawlin license."  # TODO: add real license
    author = "Alexey Eberil & Andrew Persin"
    url = ""
    description = ""  # TODO: add description
    topics = ""  # TODO: add topics

    settings = "os", "compiler", "build_type", "arch"

    options = {}
    default_options = {}

    core_sources = "CMakeTemplate/**"

    exports_sources = (
        "cmake/**",
        core_sources,
        "utils/**",
        "CMakeLists.txt",
        "README.md",
        "LICENSE",
        "VERSION",
    )

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def configure(self):
        check_min_cppstd(self, 17, gnu_extensions=False)

    def build(self):
        cmake = CMake(self)
        cmake_variables = {
            "CMAKE_EXPORT_COMPILE_COMMANDS": "ON",
            "CMAKE_TOOLCHAIN_FILE": "generators/conan_toolchain.cmake",
        }
        cmake.configure(variables=cmake_variables)
        pathlib.Path("../compile_commands").mkdir(parents=True, exist_ok=True)

        if pathlib.Path("./compile_commands.json").exists():
            shutil.copy(
                "./compile_commands.json", "../compile_commands/compile_commands.json"
            )
        cmake.build()

    def requirements(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.components["Base"].libs = ["Base"]
