import os

for i in range(2, 32):
    folder = f"Day{i}"
    os.mkdir(folder)
    for j in range(1, 3):
        open(f"{folder}/input{j}.txt", 'w').close()
        open(f"{folder}/sol{j}.py", 'w').close()