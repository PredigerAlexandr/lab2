import numpy as np


def generation(line):
    for i in range(10):
        line = np.array(list(line), dtype=np.uint8)
        neighbors1 = np.roll(line, 1, 0)
        neighbors2 = np.roll(line, 0, 0)
        neighbors3 = np.roll(line, -1, 0)
        line = np.ones(len(line), dtype=np.uint8) & \
               (((neighbors1 != 0) & (neighbors2 != 1) & (neighbors3 != 1)) |
                ((neighbors1 != 1) & (neighbors2 != 0) & (neighbors3 != 0)) |
                ((neighbors1 != 1) & (neighbors2 != 0) & (neighbors3 != 1)) |
                ((neighbors1 != 1) & (neighbors2 != 1) & (neighbors3 != 0)))
        line = np.array(line, dtype='<U32')
    line = ''.join(line)
    return line


print(
    generation("1001000101111100000101111001011011101101101111110111110000000000000011000001011001100011111101001001"))
