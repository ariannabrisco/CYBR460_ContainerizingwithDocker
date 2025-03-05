# Containerizing Applications with Docker
# Citation: https://www.geeksforgeeks.org/how-to-draw-shapes-in-matplotlib-with-python/

# Clone GitHub Repo
git clone https://github.com/ariannabrisco/CYBR460_ContainerizingwithDocker

# move into repo directory/folder
cd CYBR460_ContainerizingwithDocker 

# build image
docker build -t source .

# run image
docker run source
