import numpy as np
with open(r"resources\day8.txt") as infile:
    data = infile.readline()

data = [int(x) for x in data]

def DSN_to_layers(data,width=25, height=6):
    layers = []
    layer_counts = []
    zeros = []
    i = 0
    while  i < len(data):
        layer = np.full([height,width],99)
        for h in range(height):
            for w in range(width):
            
                layer[h,w] = data[i]
                i = i+1
                # print(h) 
        layers.append(layer) #eh, matrisförvirring
        unique, counts = np.unique(layer, return_counts=True)
        #counts_dict =dict(zip(unique, counts))
        zeros.append(counts[0])
        layer_counts.append(counts)
    # print(layers[0])
    return layers, layer_counts, zeros

layers, layer_counts, zeros = DSN_to_layers(data)

fewest_zeros = zeros.index(min(zeros))

check_Layer = layer_counts[fewest_zeros]

res=check_Layer[2]*check_Layer[1]
print(res)
##Part2

def part2(data,width=25, height=6):
    res_layer = np.full([height,width],99)
    for h in range(height):
        for w in range(width):
            for l, la in enumerate(layers):
                if la[h,w] < 2:
                    res_layer[h,w] = la[h,w]
                    break
    print(res_layer)


part2(data)
