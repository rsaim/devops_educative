# Use an image with the SDK for compilation
FROM openjdk:8-jdk-alpine as builder
WORKDIR /out

# Copy the java files to the images
COPY *.java .
# compule source code
RUN javac Hello.java

# Create a light-weight image
FROM openjdk:8-jre-alpine
# Copy compiled artifacts from the previous image
COPY --from=builder /out/*.class .
CMD ["java", "Hello"]