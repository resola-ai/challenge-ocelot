# Code Challenge: Python API Development

**Objective:**

Develop a RESTful API using Django or FastAPI framework that manages a simple "Bookstore". Your API will provide endpoints to create, read, update, and delete books in the store. Include functionality to handle user authentication to allow only registered users to modify the bookstore content.

## Requirements:

### API Functionality:

- Create a model for Books with fields: title, author, publish_date, ISBN, and price.
- Implement CRUD operations for the Books model.
- Implement user authentication: Users should register with at least an email and password.
- Only authenticated users can perform create, update, or delete operations.
- All users (authenticated or not) can list and read information about the books.

### Database:

- Use any SQL or NoSQL database of your choice to store data.

### Documentation:

- Provide a README file that includes:
  - Instructions on how to set up and run the application.
  - A brief description of the API's functionality.

### Testing:

- Write unit tests for your models and endpoints.
- Include API tests to demonstrate how each endpoint works.

### System Diagram:

- Provide a system architecture diagram showing the API, database, and any other components of your system.

### Deployment:

- Deploy your application to a free hosting provider (e.g., Heroku, PythonAnywhere, or any other).
- Provide a URL to the live API.

### Bonus (optional):

- The API needs to support a volume of 1000 requests per second in a stress test in both write and read operations.
- Can upload an image with the book cover.
- Implement rate limiting for your API.
- Add filters to list endpoints, such as filtering books by author or publish_date.
- Setup CI/CD

### Submission:

- Submit your code in a version-controlled repository (e.g., GitHub).
- Provide the system diagram as part of your repository.
- Include a Postman collection or an OpenAPI specification file to interact with the API.
- The documentation should be comprehensive and clear, suitable for new developers who are not familiar with your project.

### Evaluation Criteria:

- API should inmplement "REST API Design Best Practices". Check it out there are several good articles in the internet.
- Functionality: The API works as described in the requirements.
- Code Quality: The code is clean, modular, and follows Pythonic principles.
- Testing: The application has thorough tests, and all tests pass.
- Documentation: The documentation is clear and helpful.
- History of commits (structure and quality)
- Technical choices: Is the choice of libraries, database, architecture, etc. the best choice for the application?
- Extra Features: Implementation of the bonus features will be considered a plus.

## Doubts

Any questions you may have, please contact us by e-mail.

Godspeed! ;)
