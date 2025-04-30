# Airbnb Clone Project

## About the Project
The Airbnb Clone Project simulates a real-world booking platform to deepen understanding of full-stack development. It focuses on backend systems, database architecture, API security, and deployment practices using modern tools.

## Project Goals
- Build a scalable web application
- Practice collaborative development workflows
- Understand backend, database, and deployment best practices

## Technology Stack
- **Django**: Web framework for backend logic and RESTful APIs
- **MySQL**: Relational database for persistent storage
- **GraphQL**: Query language for efficient frontend-backend communication
- **Docker**: Containerization for consistent development environments
- **GitHub Actions**: CI/CD pipeline automation

## Team Roles
- **Backend Developer**: Builds and maintains API endpoints and business logic
- **Database Administrator (DBA)**: Designs and optimizes the relational database
- **DevOps Engineer**: Sets up CI/CD pipelines, manages deployment and automation
- **Project Manager**: Oversees project planning, coordination, and delivery timelines

## Database Design
### Key Entities and Fields
- **Users**
  - `id`: unique identifier
  - `name`: user's full name
  - `email`: login credential
  - `password_hash`: hashed password
  - `role`: user role (admin, host, guest)

- **Properties**
  - `id`: property ID
  - `title`: listing title
  - `location`: address or city
  - `price`: per-night cost
  - `owner_id`: foreign key referencing the user

- **Bookings**
  - `id`: booking ID
  - `user_id`: who made the booking
  - `property_id`: booked property
  - `start_date`: check-in date
  - `end_date`: check-out date

- **Reviews**
  - `id`: review ID
  - `user_id`: reviewer
  - `property_id`: reviewed property
  - `rating`: numeric score
  - `comment`: review content

- **Payments**
  - `id`: payment ID
  - `booking_id`: associated booking
  - `amount`: total paid
  - `status`: success or failed
  - `payment_date`: date of transaction

### Relationships
- A user can own many properties
- A user can book multiple properties
- A property can have multiple reviews and bookings
- Each booking is tied to one payment

## Feature Breakdown
- **User Management**: Users can register, log in, manage profiles, and reset passwords.
- **Property Listings**: Users can add, update, and view properties with descriptions and images.
- **Booking System**: Users can book available properties with date selection and pricing.
- **Review System**: Guests can leave reviews and ratings after a completed stay.
- **Payment Integration**: Handles secure payment processing through third-party gateways.

## API Security
- **Authentication**: JWT-based system ensures secure login and token-based access control.
- **Authorization**: Role-based permissions (e.g., guests vs. hosts) define access levels.
- **Rate Limiting**: Throttles API calls to protect against abuse and DDoS attacks.
- **Data Validation & Sanitization**: Prevents injection attacks and validates all user inputs.
- **HTTPS & Secure Headers**: Ensures all traffic is encrypted and protected from vulnerabilities.

## CI/CD Pipeline
- **Purpose**: Automates code testing and deployment, reducing manual errors and improving efficiency.
- **Tools**
  - **GitHub Actions**: Automates workflows such as testing, linting, and deployment on each push.
  - **Docker**: Ensures consistent environments across development, staging, and production.
  - **Optional Deployment Tools**: Heroku, AWS, Render, or other platforms can be used for live deployment.

---

*This project is a collaborative effort aimed at simulating a real-world software engineering environment, with a focus on learning, best practices, and full-stack proficiency.*

