cmake_minimum_required(VERSION 3.4...3.18)
project(orbslam3)

LIST(APPEND CMAKE_MODULE_PATH 
    ${PROJECT_SOURCE_DIR}/cmake
)

add_subdirectory(third_party/pybind11)
add_subdirectory(third_party/ORB_SLAM3)

pybind11_add_module(orbslam3 
    src/ORBSLAM3Wrapper.cpp
    src/NDArrayConverter.cpp
)

target_link_libraries(orbslam3
PRIVATE
    ORB_SLAM3
)

target_compile_definitions(orbslam3 
PRIVATE 
    VERSION_INFO=${EXAMPLE_VERSION_INFO}
)

target_include_directories(orbslam3
PUBLIC
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include>
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/third_party>
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/third_party/ORB_SLAM3>
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/third_party/ORB_SLAM3/include>
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/third_party/ORB_SLAM3/include/CameraModels>
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/third_party/ORB_SLAM3/Thirdparty/g2o/g2o>
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/third_party/ORB_SLAM3/Thirdparty/DBoW2/DBoW2>
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/third_party/ORB_SLAM3/Thirdparty/Sophus/sophus>
)