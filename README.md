## Tech stacks
- Django
- Django Rest Framework for API development
- Django Rest Knox for authentication
- Pytest for unit testing
- Persistent storage engine
    * Postgres on local
    * SQLite on cloud (due to platform free plan limitations)
- Docker compose for dockerization abilities


## Installation
* [How to run project locally](INSTALL.md)

## API functionality

- Create a model for Books with fields: title, author, publish_date, ISBN, and price. ✅
- Implement CRUD operations for the Books model. ✅
- Implement user authentication: Users should register with at least an email and password. ✅
- Only authenticated users can perform create, update, or delete operations. ✅
- All users (authenticated or not) can list and read information about the books. ✅

## Deployment: [Live API](https://hunghoang1110.pythonanywhere.com/api/v1/open-api/ui/)
While Heroku has an advantage of the ability of dockerizing Django apps,
I went for PythonAnywhere with traditional deployment for it's simplicity and time saving.

Free plan offered by PythonAnywhere only support SQLite so the server runs quite slow in production.

## Bonus (optional):
- Implement rate limiting for your API. ✅
- Add filters to list endpoints. ✅
    * We can filter books by genre and author last/first name
    * Example: `curl -X 'GET' \
  'https://hunghoang1110.pythonanywhere.com/api/v1/books/?genre=Novel' \
  -H 'accept: application/json'`

- Can upload an image with the book cover.
    * **AWS S3** is a popular choice of media file storage. So let's try with it.
    * There're a few ways to programmatically upload an object to an S3 bucket. I prefer "Presigned URL" approach in this case. More details:  [Boto3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html), [API](https://hunghoang1110.pythonanywhere.com/api/v1/open-api/ui/#/media/media_s3_presigned_url_create)
    * [Live demo](https://hunghoang1110.pythonanywhere.com/books/list-book/)
    * Due to time constraint, I'm not able to have a frontend page for users to manually upload images. For demo purpose, I write Python script to upload images to S3.
- Setup CI
    * Github Action does a good job at CI pipeline so I took advantage of it.
    * The CI pipeline would check coding convention (flake8, isort, etc.) enabled by [pre-commit](https://github.com/pre-commit/pre-commit) and run unit tests on new pull requests and merges on `main` branch.
    * We can check out CI runs at: https://github.com/hoangquochung1110/challenge-ocelot/actions


## Submission:
- Submit your code in a version-controlled repository (e.g., GitHub): https://github.com/hoangquochung1110/challenge-ocelot
- Include a Postman collection or an OpenAPI specification file to interact with the API: https://hunghoang1110.pythonanywhere.com/api/v1/open-api/schema/
