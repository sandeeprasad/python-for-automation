# Lists

A list stores multiple values inside a single variable.

Automation Examples

- Browser names
- Test cases
- URLs
- Status Codes
- Failed Tests

-------------------

Index

Lists start from index 0.

Example

browsers[0]

returns Chrome

-------------------

Negative Index

-1 returns the last element.

Useful for getting the latest test result.

-------------------

len()

Returns the total number of elements in a list.

- Where do we use these concepts in automation?

- Verify expected number of rows.

- Verify search results.

- Verify number of products.

- Verify number of API objects.

--------------------

append()

Automation examples

Add newly automated test cases to a regression suite.
Store failed test cases during execution.
Add API endpoints to be tested.
Add browser names for cross-browser execution.

--------------------

insert()

Automation examples

Prioritize smoke tests.
Insert high-priority test cases before execution.
Add a new environment at a specific position.
Maintain execution order.

--------------------

remove()

Automation examples

Remove obsolete test cases.
Remove unsupported browsers.
Remove inactive users from test data.
Remove deprecated API endpoints.

--------------------

pop()

Automation examples

Remove the most recently failed test.
Remove the last processed job from a queue.
Retrieve and process the latest API response.
Manage execution queues.

--------------------

updating items

Automation examples

Change execution browser.
Update environment from QA to UAT.
Modify test data.
Update URLs when environments change.

--------------------

in operator

Automation examples

Verify browser support.
Check if a test case exists before execution.
Verify environment names.
Check if an expected status code is present.
Validate user roles