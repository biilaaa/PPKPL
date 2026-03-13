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

> Graphite found no issues

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

> Graphite found no issues

## Task 3: Try adding a new model and relationships

a. Links to relevant commits/issues

> TODO

b. PR Description

> TODO

c. Graphite Diamond generated code review

> TODO

## Task 4: Improve tests for pagination and sorting

a. Links to relevant commits/issues

> TODO

b. PR Description

> TODO

c. Graphite Diamond generated code review

> TODO

## Brief Reflection

a. The types of comments you typically made in your manual reviews (e.g., correctness, performance, security, naming, test gaps, API shape, UX, docs).

> TODO

b. A comparison of **your** comments vs. **Graphite’s** AI-generated comments for each PR.

> TODO

c. When the AI reviews were better/worse than yours (cite specific examples)

> TODO

d. Your comfort level trusting AI reviews going forward and any heuristics for when to rely on them.

> TODO
