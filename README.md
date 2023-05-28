# Jokes API

## Install
- Install Pip with Python 3.8
- Create venv (`python -m venv ./venv`)
- Activate venv (`source ./venv/bin/activate` with bash/zsh)
- Install the dependencies `pip install -r requirements.txt`
- Copy-paste .env.sample and rename it .env
- Setup a local MySQL DB and update SQLALCHEMY_DATABASE_URI to set the connection string
- Run the migrations from the /db folder
  - TODO: Use alembic instead of MySQL migrations
- Set the flask entry point with `set FLASK_APP=app.py`
  - If to be run in debug mode: `set FLASK_DEBUG=1`


## API endpoints
- Get Joke:       [GET]     {hostname}/api/v1/jokes/{jokeId}
- Search Joke:    [GET]     {hostname}/api/v1/jokes/search?query={keywords}
  - keywords required, length between 3 and 120
- Delete Joke:    [DELETE]  {hostname}/api/v1/jokes/{jokeId}
- Create Joke:    [POST]    {hostname}/api/v1/jokes
  - body must contain `content` prop
- Update Joke:    [PUT]     {hostname}/api/v1/jokes/{jokeId}
  - body (optional) can contain `content` prop

## Test steps:
- Get joke:
  - Can retrieve a remote joke
  - Can retrieve a local joke
  - Can retrieve a local joke instead of the remote one if it exists
    - Get any remote joke
    - Create a local joke with the same ID
    - Get the joke again 
      - The local joke should be returned (source = local)
  - Can't retrieve a deleted local joke
    - Create local joke
    - Delete local joke
    - Try to get it
      - Should return 404 error
  - Can't retrieve a deleted remote joke
    - Delete a remote joke
    - Try to get it
      - Should return 404 error

- Search joke
  - Can retrieve both remote and local jokes
    - Create a few local jokes
      - Content
    - Search for a keyword that would match local & remote jokes
    - Should return a response containing both
  - Can't retrieve jokes without keywords
    - Should throw an informative error
  - Can't retrieve jokes outside of the range 3-120 (limit of the remote API)
    - Should throw an informative error

- Update joke:
  - Can update a local joke
    - Create a local joke
    - Update the local joke
      - The returned joke should reflect the changes
  - Can update a remote joke
    - Get a remote joke
    - Update the joke
      - The returned joke should reflect the changes
  - Can't update a joke that doesn't exist
    - Update a joke with a random ID
      - Should return 404 error
  - Can't update a deleted local joke
    - Create a local joke
    - Delete it
    - Try to fetch it
      - Should return 404 error
  - Can't update a deleted remote joke
    - Delete a remote joke
    - Try to fetch it
      - Should return 404 error

- Create joke
  - Can create a joke
    - Create a joke
    - The joke appears when fetched by ID
    - The joke appears in the search

- Delete Joke
  - Can delete remote joke
    - Delete a remote joke
    - Try to fetch it
      - Should return 404 error
    - Try to search it
      - Shouldn't appear in the returned list
  - Can delete local joke
    - Create a local joke
    - Delete the joke
    - Try to fetch it
      - Should return 404 error
    - Try to search it
      - Shouldn't appear in the returned list
  - Can't delete a joke that doesn't exist
    - Try to delete a joke that doesn't exist
      - Should return 404 error
