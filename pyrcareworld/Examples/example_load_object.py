from pyrcareworld.envs import RCareWorld

env = RCareWorld(executable_file="your_pth.x86_64", assets=["Cube"])
# if mac, something like /home/cathy/Workspace/RCareUnity/Build/TestInstall/Mac/loadObject.app/Contents/MacOS/RCareWorld
cube = env.create_object(id=12345, name="Cube", is_in_scene=False)
cube.load()
for i in range(500):
    env._step()
    print(env.instance_channel.data)
env.close()
