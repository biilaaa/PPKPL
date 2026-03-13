# Week 7 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: Zahra Nabila \
SUNet ID: **TODO** \
Citations: **TODO**

This assignment took me about **TODO** hours to do.

## Task 1: Add more endpoints and validations

a. Links to relevant commits/issues

> https://github.com/biilaaa/PPKPL/pull/1

b. PR Description

> Changes
> This PR adds additional API endpoints and improves validation and error handling for the Action Items API.

New endpoints added:

GET /action-items/{item_id}
DELETE /action-items/{item_id}
Improvements
Added proper 404 error handling when item is not found
Ensured consistent response models
Improved API structure and readability
Testing
Tested endpoints using FastAPI Swagger docs at:
http://localhost:8000/docs

Verified functionality for:

GET /action-items
GET /action-items/{id}
POST /action-items
PATCH /action-items/{id}
PUT /action-items/{id}/complete
DELETE /action-items/{id}
Notes
Endpoints were tested manually through Swagger UI to confirm correct behavior and database updates.

c. Graphite Diamond generated code review

> Graphite AI reviewed the pull request and reported that no significant issues were found. The AI confirmed that the code structure, endpoint definitions, and validation logic were implemented correctly. The review also indicated that the implementation followed common API design practices and did not detect any obvious edge cases or code quality problems.

## Task 2: Extend extraction logic

a. Links to relevant commits/issues

> https://github.com/biilaaa/PPKPL/pull/2

b. PR Description

> Changes
> Extended the action item extraction logic to detect more types of actionable sentences.

Improvements
Added detection for additional action keywords such as:

fix
update
send
create
please
remember
Example supported action items
Fix login bug
Update documentation
Send meeting notes
Please review this document
Testing
Manually tested extraction logic using sample note inputs.

c. Graphite Diamond generated code review

> Graphite AI reviewed the updated extraction logic and reported no major issues. The AI confirmed that the logic expansion improves the detection of action-oriented sentences while maintaining readability and simplicity in the implementation.

## Task 3: Try adding a new model and relationships

a. Links to relevant commits/issues

> https://github.com/biilaaa/PPKPL/pull/3

b. PR Description

> ### Changes

Added a relationship between Note and ActionItem models.

### Implementation

- Added `note_id` foreign key in ActionItem model
- Added SQLAlchemy relationships between Note and ActionItem
- A Note can now have multiple ActionItems

### Benefits

This allows action items to be associated with specific notes, improving the data model structure and enabling more meaningful relationships between stored notes and extracted tasks.

c. Graphite Diamond generated code review

> Graphite AI reviewed the database model changes and did not report any issues. The AI confirmed that the relationship definition and foreign key implementation follow standard SQLAlchemy practices.

## Task 4: Improve tests for pagination and sorting

a. Links to relevant commits/issues

> https://github.com/biilaaa/PPKPL/pull/4

b. PR Description

> ### Changes
>
> This PR improves test coverage for the Action Items API, specifically focusing on pagination and sorting functionality.

### Improvements

Two additional tests were added:

- `test_list_action_items_pagination`
  - Verifies that the `skip` and `limit` query parameters correctly control pagination.
  - Ensures the API returns the expected number of items when limits are applied.

- `test_list_action_items_sorting`
  - Verifies that the `sort` query parameter works correctly.
  - Ensures the API returns items sorted by the specified field.

### Testing

Tests were executed using `pytest` and confirmed that:

- Pagination works correctly using `skip` and `limit`.
- Sorting works correctly using `sort=-created_at`.
- Existing functionality for creating, completing, listing, and patching action items continues to work.

### Notes

These additional tests help ensure that the API behaves correctly when handling pagination and sorting parameters, improving overall test coverage and reliability.

c. Graphite Diamond generated code review

> Graphite AI reviewed the test additions and confirmed that the new tests improve coverage and do not introduce errors. The AI did not detect any issues in the test structure or API usage.

## Brief Reflection

a. The types of comments you typically made in your manual reviews (e.g., correctness, performance, security, naming, test gaps, API shape, UX, docs).

> During manual reviews, I mainly focused on the following aspects:

- Correctness of API endpoints
- Proper error handling and status codes
- Readability and structure of the code
- Consistency of response models
- Test coverage and validation logic

I also checked whether new endpoints followed the same design patterns used in the rest of the project.

b. A comparison of **your** comments vs. **Graphite’s** AI-generated comments for each PR.

> My manual review focused more on understanding the intent of the code and ensuring the API behavior matched the requirements of the assignment. I paid attention to endpoint behavior, response structures, and whether edge cases were handled properly.

Graphite’s AI review focused more on automated code analysis, such as identifying potential structural issues or code quality problems. In this assignment, the AI review reported that no significant issues were detected.

Overall, my review focused on **logic and correctness**, while the AI review focused more on **code quality and structure**.

c. When the AI reviews were better/worse than yours (cite specific examples)

> In this assignment, the AI review was useful for quickly confirming that the code did not contain obvious issues or structural mistakes. However, the AI review did not provide many detailed suggestions because the code changes were relatively straightforward.

My manual review was more helpful in understanding whether the implementation matched the functional goals of the assignment, such as ensuring the endpoints behaved correctly and that tests covered the intended functionality.

d. Your comfort level trusting AI reviews going forward and any heuristics for when to rely on them.

> After completing this assignment, I see AI code review as a helpful assistant rather than a replacement for manual review. AI can quickly detect common mistakes and confirm that code follows good structural practices, which can save time during development.

However, human review is still important for understanding the intent of the code, verifying business logic, and ensuring that the implementation matches the requirements of the project.
