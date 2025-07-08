# how to run the coverage test

- Go to group_02 folder (main folder)
- run ``$env:PYTHONPATH = "code/original-project/streamlink/src"``  

- then run ``pytest code/original-project/streamlink/src/streamlink/tests --cov=streamlink --cov-branch`` --cov-report html
    - this is if we want to make the test coverage on the test file which were written before by the developer team who created streamlink
    - to run it on our own test cases we need to change ``code/original-project/streamlink/src/streamlink/tests`` to ``code/task-3-graph/``

- then run ``start htmlcov\index.html``

