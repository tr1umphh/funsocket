install(
    TARGETS funsocket_exe
    RUNTIME COMPONENT funsocket_Runtime
)

if(PROJECT_IS_TOP_LEVEL)
  include(CPack)
endif()
