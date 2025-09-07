"""
    File with behave steps for Bing search
"""

from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError


@given('I am on bing.com')
def step_impl(context):
    raise StepNotImplementedError(u'Given I am on bing.com')


@when('I select the "Videos" category filter')
def step_impl(context):
    raise StepNotImplementedError(u'When I select the "Videos" category filter')


@then('I should see only video results related to "semrush ai"')
def step_impl(context):
    raise StepNotImplementedError(u'Then I should see only video results related to "semrush ai"')


@when('I select the "Images" category filter')
def step_impl(context):
    raise StepNotImplementedError(u'When I select the "Images" category filter')


@then('I should see only image results related to "semrush ai"')
def step_impl(context):
    raise StepNotImplementedError(u'Then I should see only image results related to "semrush ai"')


@when('I select the "Maps" category filter')
def step_impl(context):
    raise StepNotImplementedError(u'When I select the "Maps" category filter')


@then('I should see only map results related to "semrush ai"')
def step_impl(context):
    raise StepNotImplementedError(u'Then I should see only map results related to "semrush ai"')

@when('I apply an invalid time range from "1/1/9999" to "1/1/9999" date filter')
def step_impl(context):
    raise StepNotImplementedError(u'When I apply an invalid time range from "1/1/9999" to "1/1/9999" date filter')