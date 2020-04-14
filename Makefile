CDL_ROOT=/Users/gavinprivate/Git/cdl_tools_grip/tools
include ${CDL_ROOT}/lib/cdl/cdl_templates.mk
SRC_ROOT   = $(abspath ${CURDIR})
BUILD_ROOT = ${SRC_ROOT}/build
LIBRARY_NAME = atcf_hardware_std

SIM ?= $(abspath ${CURDIR})/sim

all: sim

smoke: sim
	(cd test && PATH=${SRC_ROOT}/python:${PATH} ${MAKE} SIM=${SIM} smoke)

-include ${BUILD_ROOT}/Makefile

$(eval $(call library_makefile_template,${LIBRARY_NAME},${SRC_ROOT},${BUILD_ROOT}))

clean:
	mkdir -p ${BUILD_ROOT}
