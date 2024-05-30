from conan import ConanFile


class Recipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps", "VirtualRunEnv"

    def layout(self):
        self.folders.generators = "conan"

    def requirements(self):
        self.requires("spdlog/1.14.1")
        self.requires("sqlitecpp/3.3.1")
        self.requires("asio/1.30.2")
        self.requires("capnproto/1.0.2")

    def build_requirements(self):
        self.test_requires("gtest/1.14.0")
