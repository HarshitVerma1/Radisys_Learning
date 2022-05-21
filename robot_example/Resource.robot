*** Variables ***
$(user_name) root
$(password) root123
$(host_ip) 172.27.172.3
@(values) 1 2 3 4 5 6 7
&(dict1) user=root pass=root123

***Keywords***
ADDITION
    [Arguments] ${parameter1} ${parameter2}
    ${ret_val}= Evaluate ${parameter1} + ${parameter2}
    [Return] ${ret_val}
SUITE_SETUP
    [Documentation] This is Suite Setup it will be responsible for cheching all sute cases
    log to console  ********* SUITE_SETUP started **********
SUITE_TEARDOWN
    log to console  ********* SUITE_TEARDOWN started *********
TEST_SETUP
    log to console  ********* TEST_SETUP started **********
TEST_TEARDOWN