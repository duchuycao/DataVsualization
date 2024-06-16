import plotly.graph_objects as go

def generate_bar_chart(x_data, y_data):
    fig = go.Figure(data=[go.Bar(x=x_data, y=y_data)])
    fig.update_layout(title='Interactive Bar Chart',
                      xaxis_title='X Axis',
                      yaxis_title='Y Axis')
    return fig

# Example user input (you can modify this to take input from users dynamically)
x_data = ['A', 'B', 'C', 'D']
y_data = [10, 20, 15, 25]

# Generate the interactive visualization
fig = generate_bar_chart(x_data, y_data)

# Save the HTML file for the visualization
fig.write_html('index.html')
