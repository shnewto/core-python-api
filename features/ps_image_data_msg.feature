# WARNING: Auto-generated file. Any changes are subject to being overwritten
# by setup.py build script.

Feature: ps_image_data_msg support
	Scenario: Excercise PolySync message conversion between Python API and C API
		Given I have a Py_ps_image_data_msg object
		When I convert it to its C API equivalent a ps_image_data_msg
		And I convert the ps_image_data_msg back to a Py_ps_image_data_msg
		Then the ps_image_data_msg values are equivalent to each Py_ps_image_data_msg value

	Scenario: Excercise Python API publish type check
		Given a ps_image_data_msg.publish function exists
		When I try to publish something that is not of type Py_ps_image_data_msg
		Then a TypeError indicates the type was not Py_ps_image_data_msg

	Scenario: Excercise Py_ps_image_data_msg publish and subscribe
		Given I have a licensed PsNode for publishing Py_ps_image_data_msg
		And I have a Py_ps_image_data_msg
		And I have a handler for Py_ps_image_data_msg subscription
		When I publish my Py_ps_image_data_msg
		Then I receive the corresponding Py_ps_image_data_msg in my handler
