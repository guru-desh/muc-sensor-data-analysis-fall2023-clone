import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def plot_data(data):
    plt.title('X,Y,Z Plot')
    plt.plot([row[0] for row in data],[row[1] for row in data], label="x")
    plt.plot([row[0] for row in data],[row[2] for row in data], label="y")
    plt.plot([row[0] for row in data],[row[3] for row in data], label="z")
    plt.legend(loc='upper right')
    plt.show()


def plot_data_plotly(data, title=None):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[row[0] for row in data], y=[row[1] for row in data],
                        mode='lines',
                        name='x'))
    fig.add_trace(go.Scatter(x=[row[0] for row in data], y=[row[2] for row in data],
                        mode='lines',
                        name='y'))
    fig.add_trace(go.Scatter(x=[row[0] for row in data], y=[row[3] for row in data],
                        mode='lines',
                        name='z'))
    fig.update_layout(
        title=title,
        xaxis_title="Time",
        yaxis_title="Acceleration"
    )

# plot_data("test.csv")
