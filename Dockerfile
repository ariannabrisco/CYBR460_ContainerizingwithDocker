# Use python as the language
FROM python:3

# Create directory
WORKDIR /CYBR460_ContainerizingwithDocker

# Clone GitHub repo
RUN git clone https://github.com/ariannabrisco/CYBR460_ContainerizingwithDocker /app

# Copy code file in current folder
COPY source.py .

# Install python library matplotlib
RUN pip install matplotlib

# Run code
CMD ["python3", "./source.py"]
