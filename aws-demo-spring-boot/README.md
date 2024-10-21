# AWS Demo Spring Boot Application

This is a demo Spring Boot application migrated from an EJB3 bean.

## How to Run

1. Clone the repository.
2. Run `mvn clean install` to build the project.
3. Run `mvn spring-boot:run` to start the application.
4. Access the application at `http://localhost:8080/hello`.

## CI/CD Pipeline

The CI/CD pipeline is configured using Jenkins. The pipeline includes steps for building, testing, and deploying the application.

## Deployment

The application is deployed to AWS ECS using Terraform. The deployment script is located in the `terraform` directory.
