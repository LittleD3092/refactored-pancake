# Install script for directory: /home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/itron/refactored-pancake/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fkie_multimaster_msgs/msg" TYPE FILE FILES
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/msg/LinkState.msg"
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/msg/LinkStatesStamped.msg"
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/msg/MasterState.msg"
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/msg/ROSMaster.msg"
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/msg/SyncMasterInfo.msg"
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/msg/SyncServiceInfo.msg"
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/msg/SyncTopicInfo.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fkie_multimaster_msgs/srv" TYPE FILE FILES
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/srv/DiscoverMasters.srv"
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/srv/GetSyncInfo.srv"
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/srv/LoadLaunch.srv"
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/srv/Task.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fkie_multimaster_msgs/cmake" TYPE FILE FILES "/home/itron/refactored-pancake/catkin_ws/build/multimaster/fkie_multimaster_msgs/catkin_generated/installspace/fkie_multimaster_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/itron/refactored-pancake/catkin_ws/devel/include/fkie_multimaster_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/itron/refactored-pancake/catkin_ws/devel/share/roseus/ros/fkie_multimaster_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/itron/refactored-pancake/catkin_ws/devel/share/common-lisp/ros/fkie_multimaster_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/itron/refactored-pancake/catkin_ws/devel/share/gennodejs/ros/fkie_multimaster_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/itron/refactored-pancake/catkin_ws/devel/lib/python3/dist-packages/fkie_multimaster_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/itron/refactored-pancake/catkin_ws/devel/lib/python3/dist-packages/fkie_multimaster_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/itron/refactored-pancake/catkin_ws/build/multimaster/fkie_multimaster_msgs/catkin_generated/installspace/fkie_multimaster_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fkie_multimaster_msgs/cmake" TYPE FILE FILES
    "/home/itron/refactored-pancake/catkin_ws/build/multimaster/fkie_multimaster_msgs/catkin_generated/installspace/fkie_multimaster_msgs-msg-extras.cmake"
    "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/cmake/version.cmake.in"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fkie_multimaster_msgs/cmake" TYPE FILE FILES
    "/home/itron/refactored-pancake/catkin_ws/build/multimaster/fkie_multimaster_msgs/catkin_generated/installspace/fkie_multimaster_msgsConfig.cmake"
    "/home/itron/refactored-pancake/catkin_ws/build/multimaster/fkie_multimaster_msgs/catkin_generated/installspace/fkie_multimaster_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fkie_multimaster_msgs" TYPE FILE FILES "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/fkie_multimaster_msgs" TYPE DIRECTORY FILES "/home/itron/refactored-pancake/catkin_ws/devel/lib/python3/dist-packages/fkie_multimaster_msgs/grpc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fkie_multimaster_msgs" TYPE DIRECTORY FILES "/home/itron/refactored-pancake/catkin_ws/src/multimaster/fkie_multimaster_msgs/grpc")
endif()

