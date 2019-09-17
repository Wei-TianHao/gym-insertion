#!/usr/bin/env python3
"""
Example of how bodies interact with each other. For a body to be able to
move it needs to have joints. In this example, the "robot" is a red ball
with X and Y slide joints (and a Z slide joint that isn't controlled).
On the floor, there's a cylinder with X and Y slide joints, so it can
be pushed around with the robot. There's also a box without joints. Since
the box doesn't have joints, it's fixed and can't be pushed around.
"""
from mujoco_py import load_model_from_xml, MjSim, MjViewer
import math
import os

MODEL_XML = """
<?xml version="1.0" ?>
<mujoco>
    <option timestep="0.005" gravity="0 0 -9.8" solver="CG"/>
    <worldbody>

        <body name="part" pos="0 0 2.5">
            <joint type="ball" name="r"/>
            <joint axis="1 0 0" damping="0.1" name="x" pos="0 0 0" type="slide"/>
            <joint axis="0 1 0" damping="0.1" name="y" pos="0 0 0" type="slide"/>
            <joint axis="0 0 1" damping="1" name="z" pos="0 0 0" type="slide"/>
            
			<geom conaffinity="0" contype="1" pos="0 0 0" rgba="1.0 1.0 1.0 1" size="0.3 0.2 0.1" type="box" mass="10.0"></geom>
            <body name="pin">
                <geom conaffinity="0" contype="1" pos="0.2  0.1 -0.1" rgba="1.0 1.0 1.0 1" size="0.02 0.02 0.2" type="box" mass="1.0"></geom>
                <geom conaffinity="0" contype="1" pos="0.2 -0.1 -0.1" rgba="1.0 1.0 1.0 1" size="0.02 0.02 0.2" type="box" mass="1.0"></geom>
                <geom conaffinity="0" contype="1" pos="0.2  0.0 -0.1" rgba="1.0 1.0 1.0 1" size="0.02 0.02 0.2" type="box" mass="1.0"></geom>
            </body>
		</body>
        
        <body name="board" pos="0 0 -0.1">
            <geom condim="3" pos="0.52 0 0"  size="0.3 1.0 0.1" rgba="0 1 0 0.5" type="box"/>
            <geom condim="3" pos="0.20 -0.57 0"  size="0.03 0.43 0.1" rgba="0 1 0 1" type="box"/>
            <geom condim="3" pos="0.20  0.57 0"  size="0.03 0.43 0.1" rgba="0 1 0 1" type="box"/>

            <geom condim="3" pos="-0.325 0 0" size="0.5 1.0 0.1" rgba="0 1 0 1" type="box"/>
            <geom condim="3" pos="0.20 -0.15 0"  size="0.03 0.025 0.1" rgba="0 1 0 1" type="box"/>
            <geom condim="3" pos="0.20  0.15 0"  size="0.03 0.025 0.1" rgba="0 1 0 1" type="box"/>
            <geom condim="3" pos="0.20  0.05 0"  size="0.03 0.025 0.1" rgba="0 1 0 1" type="box"/>
            <geom condim="3" pos="0.20 -0.05 0"  size="0.03 0.025 0.1" rgba="0 1 0 1" type="box"/>
		</body>
        0.02 0.08
    

    </worldbody>
    <actuator>
        <motor gear="1" joint="x" name="x_m"/>
        <motor gear="1" joint="y" name="y_m"/>
        <motor gear="1" joint="z" name="z_m"/>

        <motor gear="1 0 0" joint="r" name="r_x"/>
        <motor gear="0 1 0" joint="r" name="r_y"/>
        <motor gear="0 0 1" joint="r" name="r_z"/>
    </actuator>
</mujoco>
"""

model = load_model_from_xml(MODEL_XML)
sim = MjSim(model)
viewer = MjViewer(sim)
t = 0
while True:
    # sim.data.ctrl[0] = 1
    # sim.data.ctrl[1] = 1
    # sim.data.ctrl[2] = 1
    # sim.data.ctrl[3] = math.cos(t) * 5
    # sim.data.ctrl[4] = math.cos(t) * 5
    # sim.data.ctrl[5] = math.cos(t) * 5
    t += 1
    sim.step()
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break