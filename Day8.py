from aocd import data
import re
import pandas as pd

def chunkstring(string, length):
  return re.findall('.{%d}' % length, string)

def image_decoder(x,y,layers_ls):
    """
    goes through layers_ls at that x,y coordinate and returns the first pixel that is non-transparent
    :param x:
    :param y:
    :param layers_ls:
    :return: 0,1, or 2
    """
    for layer in layers_ls:
        if layer.loc[x,y]=='1':
            return int(1)
        elif layer.loc[x,y]=='0':
            return int(0)
    return int(2)

if __name__=="__main__":
    num_layers=len(data)//(25*6)
    layers=chunkstring(data,25*6)

    #part1
    """min_0s=(0,layers[0].count("0"))
    for i in range(1,len(layers)):
        if layers[i].count("0")<min_0s[1]:
            min_0s=(i,layers[i].count("0"))
    layer=min_0s[0]
    num_1s=layers[layer].count("1")
    num_2s=layers[layer].count("2")
    multiple=num_1s*num_2s"""

    #part2
    layers_ls=[]#list to hold dataframes of layers
    for layer in layers:
        rows=chunkstring(layer,25)
        split_rows=[]
        for row in rows:
            split_row=[x for x in row]
            split_rows.append(split_row)
        layers_ls.append(pd.DataFrame(split_rows))

    final_image_df=pd.DataFrame()
    for x in range(0,6):#rows
        for y in range(0,25):#cols
            final_image_df.loc[x,y]=image_decoder(x,y,layers_ls)


    print("foo")

    print("done")