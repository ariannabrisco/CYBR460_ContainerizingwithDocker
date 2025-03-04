# Use Ubuntu operating system, latest version
FROM ubuntu:latest

# Use python as the language
FROM python:3

# Clone GitHub repo
RUN git clone https://github.com/ariannabrisco/CYBR_460

# Create directory
WORKDIR /Assignment3

# Install python library matplotlib
RUN pip install matplotlib

# Run code
CMD ["python", 'source.py']
