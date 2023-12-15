# Reaction-Diffusion Simulation (Work In Process)

## Overview
<p float="center">
This Python script simulates various reaction-diffusion models, with a focus on the Gray-Scott model. It can generate images and animations to visualize the complex patterns formed by these models. 
  <img src="https://github.com/Songhyeane/OpenSourceProject24-7/assets/50310635/a74d5493-d6ad-47f4-ade5-b8e3ea2a1d76" width="400" />
</p>

## Demo
We have the capability to utilize a Canny edge detector to compute the contour of a human figure and apply it as a seed point in various computational simulations or image processing tasks. The Canny edge detector, a widely used algorithm in the field of computer vision, excels in identifying the edges and contours within an image by detecting areas of rapid intensity change.

When applied to an image of a human figure, this algorithm can precisely outline the human shape. By doing so, it transforms the human figure into a distinct set of edges, which can be used as seed points. Seed points are crucial in various applications, particularly in simulations or processes that involve growth patterns, reaction-diffusion systems, or other forms of pattern development. For instance, in a reaction-diffusion simulation, these seed points derived from the human contour can be the starting points for the simulation to evolve, leading to unique patterns that are influenced by the shape of the human figure.

This technique opens up a multitude of possibilities for creative and scientific explorations. In artistic domains, it can be used to create visually striking patterns that retain the essence of the human form. In scientific research, particularly in fields like bioinformatics or materials science, this method can be instrumental in studying pattern formation and development influenced by complex shapes like that of the human body.

Moreover, the adaptability of the Canny edge detector allows for its application across various image types and qualities, making it a versatile tool in both artistic and scientific endeavors. By leveraging the human contour as a seed point, we can explore a fascinating intersection of art, science, and technology.

------
### Original Image
![image](https://github.com/Songhyeane/OpenSourceProject24-7/assets/50310635/cf2bda74-bf24-41cf-b3cf-14c9a9821271)

### Generated Pattern
<p float="center">
  <img src="https://github.com/Songhyeane/OpenSourceProject24-7/assets/50310635/f9e43727-0168-42d7-b297-6397a493a1c7" width="400" />
</p>
![KakaoTalk_20231215_192257586](https://github.com/Songhyeane/OpenSourceProject24-7/assets/50310635/f9e43727-0168-42d7-b297-6397a493a1c7)

## Installation
- Ensure Python is installed on your system.
- Install required Python libraries: `numpy`, `matplotlib`, `argparse`, `cv2`.
- Download the script and any additional resources.

## Usage
Run the script with Python from the command line. Here are some example usages:
- `python ReactionDiffusion.py -o my_simulation --moviemode -n 10000`
- `python ReactionDiffusion.py -o my_simulation2 -m GM -n 5000`

### Command Line Arguments
- `-o`, `--outname`: Set the output name for the simulation run.
- `-mov`, `--moviemode`: Enable movie mode to store sequential images (default: off).
- `-n`, `--timesteps`: Set the number of timesteps for the simulation (default: 8000).
- `-m`, `--model`: Choose the model for simulation (`FN`, `GM`, `GS`).

## Creating Specific Patterns in the Gray-Scott Model

### Step 1: Choose a Specific Pattern
Identify the type of pattern you want to create, like solitons, coral, maze, waves, flicker, or worms.

### Step 2: Set Parameters
Set the parameters (`Du`, `Dv`, `F`, `k`) based on your chosen pattern. Example for a maze pattern:
```python
params = {
    "Du": 0.19, 
    "Dv": 0.05, 
    "F": 0.06, 
    "k": 0.062,
    "myCmap": plt.cm.cubehelix,
    "edgeMax": False,
    "dt": 1,
    "dx": 1
}
```

### Step 3: Initialize the Simulation Grid
Set the initial values for U and V matrices. You can choose from single spot, dual spots, or random noise.

### Step 4: Run the Simulation
Run the simulation with the set parameters and initial conditions for the desired number of timesteps.

### Step 5: Generate Output Images
The script will generate images at specified intervals, visualizing the pattern evolution.

## Output (Simple boundary condition)
The script generates a series of images representing the state of the system at various timesteps.

<p float="left">
  <img src="https://github.com/Songhyeane/OpenSourceProject24-7/assets/50310635/c3efad71-f63a-4659-8fbe-8d5eaeb38a5e" width="400" />
  <img src="https://github.com/Songhyeane/OpenSourceProject24-7/assets/50310635/8fad7338-9fc5-40b3-9f0b-e1f032eaaa0b" width="400" /> 
</p>
