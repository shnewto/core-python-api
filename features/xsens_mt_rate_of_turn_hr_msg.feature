# WARNING: Auto-generated file. Any changes are subject to being overwritten
# by setup.py build script.

Feature: xsens_mt_rate_of_turn_hr_msg support
	Scenario: Excercise PolySync message conversion between Python API and C API
		Given I have a Py_xsens_mt_rate_of_turn_hr_msg object
		When I convert it to its C API equivalent a xsens_mt_rate_of_turn_hr_msg
		And I convert the xsens_mt_rate_of_turn_hr_msg back to a Py_xsens_mt_rate_of_turn_hr_msg
		Then the xsens_mt_rate_of_turn_hr_msg values are equivalent to each Py_xsens_mt_rate_of_turn_hr_msg value

	Scenario: Excercise Python API publish type check
		Given a xsens_mt_rate_of_turn_hr_msg.publish function exists
		When I try to publish something that is not of type Py_xsens_mt_rate_of_turn_hr_msg
		Then a TypeError indicates the type was not Py_xsens_mt_rate_of_turn_hr_msg

	Scenario: Excercise Py_xsens_mt_rate_of_turn_hr_msg publish and subscribe
		Given I have a licensed PsNode for publishing Py_xsens_mt_rate_of_turn_hr_msg
		And I have a Py_xsens_mt_rate_of_turn_hr_msg
		And I have a handler for Py_xsens_mt_rate_of_turn_hr_msg subscription
		When I publish my Py_xsens_mt_rate_of_turn_hr_msg
		Then I receive the corresponding Py_xsens_mt_rate_of_turn_hr_msg in my handler
