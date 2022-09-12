# import numpy
# from matplotlib import pyplot
# w = numpy.array([[0,1,1,1,0],
# [1,0,1,0,1],
# [1,1,0,1,0],
# [1,0,1,0,0],
# [0,1,0,0,0]
# ])
# value = numpy.array([2,10,1,4,7])
# stdValue = ( value - numpy.mean(value) ) / numpy.std(value)
# lagedValue = numpy.matmul(stdValue, w)
# pyplot.scatter(stdValue, lagedValue)
# pyplot.show()

import matplotlib.pyplot as plt
from libpysal.weights.contiguity import Queen
from libpysal import examples
import geopandas as gpd
from esda.moran import (Moran, Moran_BV,
                        Moran_Local, Moran_Local_BV)
from splot.esda import moran_scatterplot
gdf = gpd.read_file("./test_moran.gpkg")
x = gdf['value'].values
w = Queen.from_dataframe(gdf)
w.transform = 'r'
moran = Moran(x, w)
moran_scatterplot(moran, p=0.05)
plt.show()
