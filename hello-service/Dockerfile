# Use an official Java runtime as a parent image
FROM openjdk:22-jdk

# Set the working directory inside the container
WORKDIR /app

# Copy the jar file into the container at /app
COPY target/*.jar app.jar

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the jar file
ENTRYPOINT ["java","-jar","/app/app.jar"]

