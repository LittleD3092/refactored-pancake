execute_process(COMMAND "/home/itron/refactored-pancake/catkin_ws/build/multimaster/fkie_node_manager/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/itron/refactored-pancake/catkin_ws/build/multimaster/fkie_node_manager/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
