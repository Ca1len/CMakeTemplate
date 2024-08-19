from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import load
import os


class CMakeTemplate(ConanFile):
    name = "cmake_template"

    license = ""  # TODO: add real license
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
        "package_info.toml",
    )

    def set_version(self):
        try:
            self.version = load(self, "VERSION").strip()
        except FileNotFoundError:
            self.version = load(self, "../VERSION").strip()

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
        cmake.configure()
        cmake.build()

    def requirements(self):
        self.requires("fmt/9.1.0")

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        # self.conanutils.parse_package_info(self, "package_info.toml")
        self.cpp_info.components["base"].libs = ["base"]
