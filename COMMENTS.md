# Comments

## Things that could have been added
- Add CI/CD step to run DB migrations and deploy the app
- Integrate other source of joke, e.g. https://icanhazdadjoke.com/api
- Unit tests 
  - Update joke: to spy if we are retrieving the remote joke if it doesn't exist locally and create it locally
  - Delete joke: to spy if we are creating the joke and then deleting it if it doesn't exist locally
- Add logging with Sentry or similar tool
- Add documentation (Swagger, etc.)
- Add a /jokes/random
- Add categories filters on search (only include & exclude categories)
- Add upvote/downvote of jokes
- Add an abstract repository layer between services and DB requests to abstract the usage of SQLAlchemy
  - De-prioritized that because unnecessary in small scope projects. Would become a priority if we were to add other data-source (e.g Bucket, Another type of DB such as NoSQL, etc.) or if the scope increased to use more than a few services.


## How to add a joke source?
- The app was built to be able to replace the chuck norris joke source by another. To accomplish that:
  - Create a new third-party joke provider under `/third_parties/jokes` that is a class inheriting from `base_joke_api`
  - Update `/third_parties/jokes/remote_joke_api.py` to update the rules that uses X or Y joke provider (can use the env var `REMOTE_JOKE_TYPE`)

## On the folder structure
- The business logic is split by service under the root folder, like `/jokes`.
  -  if we were to add users, we would need to create a module under `/users`.
- The `/lib` folder contains the configuration of external dependencies that are used to execute our business logic (DB, rest api, etc.)
- `/db` contains the DB schema migration
  - Ultimately, we should have a subfolder `/migrations` and `/data` to avoid mixing data scripts and schema migrations
  - Could have mocked the DB, but I think it is important for engineers to demonstrate how they handle changes in app's data layer
- `/third_parties` contains code to interact with remote services on which our app is depending on
  - If we were to add some cloud provider services, let's say AWS SQS, we would create something such as `/third_parties/queue.py` so we wouldn't mix our business logic with implementation details (like configuring the SDK, etc.)

## Libraries used
- Cerberus: To validate the incoming requests, used because of familiarity
- SQLAlchemy & PyMySQL & MySQL DB: Used for familiarity related to my current work
