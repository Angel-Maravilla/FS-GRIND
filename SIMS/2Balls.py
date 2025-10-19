import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    xpos: float
    ypos: float
    xvel: float
    yvel: float

deltaT = 0.04
bounceCoeff = 0.9

def step(state: State) -> State:
    new_xpos = state.xpos + state.xvel * deltaT
    new_ypos = state.ypos + state.yvel * deltaT
    new_yvel = state.yvel - 9.81 * deltaT
    if new_ypos < 0:
        new_ypos = 0
        new_yvel = -new_yvel * bounceCoeff
    return State(new_xpos, new_ypos, state.xvel, new_yvel)

two_balls = [                               ##2 balls
    State(xpos=-0.7, ypos=4.0, xvel=0,  yvel=0.0),       
    State(xpos= 0.4, ypos=2.0, xvel=0, yvel=1.0),
] 

fig = plt.figure(figsize=(3,3), dpi=150)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(-2, 2)
ax.set_ylim(0, 8)

scat = ax.scatter([], [], s=200)

def animate(i):
    global two_balls, scat
    two_balls = [step(b) for b in two_balls]
    xs = [b.xpos for b in two_balls]
    ys = [b.ypos for b in two_balls]
    scat.set_offsets(np.c_[xs, ys])
    return scat,

an = animation.FuncAnimation(fig, animate, interval=16, cache_frame_data=False)
plt.show()