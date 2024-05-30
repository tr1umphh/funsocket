# Parent project does not export its library target, so this CML implicitly
# depends on being added from it, i.e. the testing is done only from the build
# tree and is not feasible from an install location

project(funsocketTests LANGUAGES CXX)

# ---- Dependencies ----

find_package(GTest REQUIRED)

# ---- Tests ----

add_executable(funsocket_test source/funsocket_test.cpp)
target_link_libraries(
    funsocket_test PRIVATE
    gtest::gtest
)
target_compile_features(funsocket_test PRIVATE cxx_std_17)

# ---- End-of-file commands ----

add_folders(Test)
