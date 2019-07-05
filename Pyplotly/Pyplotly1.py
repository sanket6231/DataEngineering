import plotly
import plotly.graph_objs as go
import plotly.offline as pyo

# Create random data with numpy
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

data = [go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers'
)]

pyo.plot(data, filename='basic-scatter')
