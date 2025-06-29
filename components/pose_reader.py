# CODE#03
#⚙️ In real-world, we can use CLIP, BLIP, or MediaPipe Pose to understand uploaded images
# We'll simulate a small function that "describes" the uploaded pose using fake outputs (can later be replaced with CLIP):

import random

def mock_pose_analysis():
    poses = [
        "Standing with one hand on hip",
        "Sitting cross-legged",
        "Walking with casual smile",
        "Leaning against wall",
        "Side pose with tilted head"
    ]
    return random.choice(poses)
