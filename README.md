# Amygdale_

This is an Image Archiving Project, which aims to achieve a theoretical compression rate of over 80%.

# How it Works

A 256x256x256 grid is mapped, with each axis representing R G B, with every RGB value corresponding to the co-ordinates of the blocks in the grid.
The dominating colours of the image are clustered into bubbled regions on the grid with the help of k-means clustering.
