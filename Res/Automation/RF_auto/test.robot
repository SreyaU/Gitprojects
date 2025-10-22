*** Settings ***
Library    BuiltIn

*** Test Cases ***
My First Test
    [Documentation]    A simple test case that always passes
    Log    Hello, Robot Framework!
    ${result}=    Evaluate    2 + 2
    Should Be Equal As Integers    ${result}    4