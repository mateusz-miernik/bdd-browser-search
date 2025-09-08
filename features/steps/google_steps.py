"""
    File with behave steps for Google search
"""

from behave import when, then
from behave.exception import StepNotImplementedError


@when('I search for "{query}"')
def step_impl(context, query):
    context.page_obj.search(query)

@when('I apply the "{date_filter}" date filter')
def step_impl(context, date_filter):
    context.page_obj.apply_date_filter(date_filter)

@then('I should see results published within the last week related to "{query}"')
def step_impl(context, query):
    assert context.page_obj.results_within_last_week(query), \
        f"Expected results within last week for {query}, but got none."

@then('I should see a message indicating "{query]"')
def step_impl(context, query):
    raise StepNotImplementedError(u'Then I should see a message indicating "No results found"')

@then('I should be provided with suggestions to broaden the date filter')
def step_impl(context):
    raise StepNotImplementedError('Then I should be provided with suggestions to broaden the date filter')

@then('I should see results published within the last 24 hours related to "prowly ai"')
def step_impl(context):
    raise StepNotImplementedError(u'Then I should see results published within the last 24 hours related to "prowly ai"')

@when('no results are available in that time range')
def step_impl(context):
    raise StepNotImplementedError(u'When no results are available in that time range')

@then('I should see a message indicating "No results found"')
def step_impl(context):
    raise StepNotImplementedError(u'Then I should see a message indicating "No results found"')
