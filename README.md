# Containerizing Applications with Docker
# Citation: https://www.geeksforgeeks.org/how-to-draw-shapes-in-matplotlib-with-python/

# STEP 1: Open terminal or command line

# Step 1.1: Clone GitHub Repo
git clone https://github.com/ariannabrisco/CYBR460_ContainerizingwithDocker

# Step 1.2: Move into repo directory/folder
cd CYBR460_ContainerizingwithDocker 

# Step 1.3: Build image
docker build -t generate_bluegold .

# Step 1.4: run image
docker run generate_bluegold

# Step 1.5: Open Visual Studio Code
code .

# Step 2: Open source.py
Click on source.py in explorer sidebar

# Step 2.1: Run source.py
Click on run button

# Step 3: Confirm output
Click on blue_gold.jpg and compare with expected_output_blue_gold.jpg
