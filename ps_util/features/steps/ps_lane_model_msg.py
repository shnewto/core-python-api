# WARNING: Auto-generated file. Any changes are subject to being overwritten
# by setup.py build script.

#!/usr/bin/python
import time
from behave import given
from behave import when
from behave import then
from hamcrest import assert_that, equal_to

try:
    import polysync.node as ps_node
    from polysync.data_model.types import Py_ps_lane_model_msg
    from polysync.data_model._internal.compare import ps_lane_model_msg_type_convert_testable, Py_ps_lane_model_msg_initialize_random
    from polysync.data_model.message_support.ps_lane_model_msg import publish, subscribe
except ImportError:
    raise ImportError(
        'Py_ps_lane_model_msg module dependencies \
        missing for tests, is the project built?')


@given('I have a Py_ps_lane_model_msg object')
def step_impl(context):
    pass

@when('I convert it to its C API equivalent a ps_lane_model_msg')
def step_impl(context):
    pass

@when('I convert the ps_lane_model_msg back to a Py_ps_lane_model_msg')
def step_impl(context):
    pass

@then('the ps_lane_model_msg values are equivalent to each Py_ps_lane_model_msg value')
def step_impl(context):
    msg = Py_ps_lane_model_msg_initialize_random()
    result = ps_lane_model_msg_type_convert_testable(msg)
    assert not result, result

@given('a ps_lane_model_msg.publish function exists')
def step_impl(context):
    assert callable(publish)

@when('I try to publish something that is not of type Py_ps_lane_model_msg')
def step_impl(context):
    bad_obj = "not the right type of object!"
    context.exception = None

    try:
        publish(bad_obj)
    except Exception as e:
        context.exception = e

@then('a {exeption} indicates the type was not Py_ps_lane_model_msg')
def step_impl(context, exeption):
    assert isinstance(context.exception, eval(exeption)), \
    "Invalid exception %s - expected %s" \
    % (type(context.exception).__name__, exeption)

GLOBAL_TIMESTAMP = None
GLOBAL_GUID = None

def Py_ps_lane_model_msg_handler(msg):
    if msg.header.src_guid == GLOBAL_GUID:
        global GLOBAL_TIMESTAMP
        GLOBAL_TIMESTAMP = msg.header.timestamp

@given(u'I have a licensed PsNode for publishing Py_ps_lane_model_msg')
def step_impl(context):
    assert context.node_ref
    global GLOBAL_GUID
    GLOBAL_GUID = context.my_guid

@given(u'I have a Py_ps_lane_model_msg')
def step_impl(context):
    context.msg = Py_ps_lane_model_msg()
    context.msg.header.timestamp = 0xFFFF

@given(u'I have a handler for Py_ps_lane_model_msg subscription')
def step_impl(context):
    assert Py_ps_lane_model_msg_handler
    subscribe(handler=Py_ps_lane_model_msg_handler)

@when(u'I publish my Py_ps_lane_model_msg')
def step_impl(context):
    publish(context.msg)

@then(u'I receive the corresponding Py_ps_lane_model_msg in my handler')
def step_impl(context):
    global GLOBAL_TIMESTAMP
    while not GLOBAL_TIMESTAMP:
        time.sleep(1)
    assert_that(context.msg.header.timestamp, equal_to(GLOBAL_TIMESTAMP))

