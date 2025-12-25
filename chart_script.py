import plotly.graph_objects as go
import plotly.express as px

# Define the CI/CD pipeline stages with better spacing
stages = [
    {"id": 1, "name": "Dev Commit", "type": "start", "x": 0, "y": 8, "color": "#4CAF50"},
    {"id": 2, "name": "CI Trigger", "type": "process", "x": 3, "y": 8, "color": "#2196F3"},
    {"id": 3, "name": "Checkout", "type": "process", "x": 6, "y": 8, "color": "#2196F3"},
    {"id": 4, "name": "Dependencies", "type": "process", "x": 9, "y": 8, "color": "#2196F3"},
    {"id": 5, "name": "Unit Tests", "type": "decision", "x": 12, "y": 8, "color": "#FFC107"},
    {"id": 6, "name": "Quality Check", "type": "decision", "x": 15, "y": 8, "color": "#FFC107"},
    {"id": 7, "name": "Security Scan", "type": "decision", "x": 18, "y": 8, "color": "#FFC107"},
    {"id": 8, "name": "Build Image", "type": "process", "x": 21, "y": 8, "color": "#2196F3"},
    {"id": 9, "name": "Push Registry", "type": "process", "x": 24, "y": 8, "color": "#2196F3"},
    {"id": 10, "name": "Deploy Staging", "type": "process", "x": 27, "y": 8, "color": "#009688"},
    {"id": 11, "name": "Integration Test", "type": "decision", "x": 30, "y": 8, "color": "#FFC107"},
    {"id": 12, "name": "Manual Approval", "type": "decision", "x": 33, "y": 8, "color": "#FFC107"},
    {"id": 13, "name": "Deploy Prod", "type": "process", "x": 36, "y": 8, "color": "#4CAF50"},
    {"id": 14, "name": "Health Check", "type": "decision", "x": 39, "y": 8, "color": "#FFC107"},
    {"id": 15, "name": "Monitoring", "type": "end", "x": 42, "y": 8, "color": "#00BCD4"},
    {"id": 16, "name": "Rollback", "type": "process", "x": 39, "y": 4, "color": "#F44336"},
    {"id": 17, "name": "Notify Team", "type": "process", "x": 21, "y": 4, "color": "#F44336"}
]

# Create the figure
fig = go.Figure()

# Add main success path with prominent line
main_path_x = [s["x"] for s in stages[:15]]
main_path_y = [s["y"] for s in stages[:15]]

fig.add_trace(go.Scatter(
    x=main_path_x,
    y=main_path_y,
    mode='lines',
    line=dict(color='#4CAF50', width=4),
    name='Success Path',
    showlegend=False
))

# Add failure paths with distinct styles
failure_stages = [5, 6, 7, 11, 12]  # Stages that can fail
notify_stage = stages[16]  # Notify Team stage

for i, stage_id in enumerate(failure_stages):
    stage = stages[stage_id-1]
    # Use different dash patterns for different failure paths
    dash_style = ['dot', 'dash', 'dashdot'][i % 3]
    fig.add_trace(go.Scatter(
        x=[stage["x"], notify_stage["x"]],
        y=[stage["y"], notify_stage["y"]],
        mode='lines',
        line=dict(color='#F44336', width=3, dash=dash_style),
        name='Failure Path',
        showlegend=False
    ))

# Add rollback path with prominent styling
health_stage = stages[13]   # Health Check
rollback_stage = stages[15]  # Rollback

fig.add_trace(go.Scatter(
    x=[health_stage["x"], rollback_stage["x"], notify_stage["x"]],
    y=[health_stage["y"], rollback_stage["y"], notify_stage["y"]],
    mode='lines',
    line=dict(color='#F44336', width=4, dash='solid'),
    name='Rollback Path',
    showlegend=False
))

# Add prominent feedback loop
fig.add_trace(go.Scatter(
    x=[notify_stage["x"], stages[0]["x"]],
    y=[notify_stage["y"], stages[0]["y"]],
    mode='lines',
    line=dict(color='#FF9800', width=4, dash='longdash'),
    name='Feedback Loop',
    showlegend=False
))

# Add curved arrow for feedback loop to make it more prominent
fig.add_annotation(
    x=10, y=2,
    ax=notify_stage["x"], ay=notify_stage["y"]-0.5,
    xref="x", yref="y",
    axref="x", ayref="y",
    showarrow=True,
    arrowhead=2,
    arrowsize=2,
    arrowwidth=3,
    arrowcolor="#FF9800",
    text="Fix & Retry",
    font=dict(size=12, color="#FF9800")
)

# Add stage markers with larger size
for stage in stages:
    # Determine marker shape based on type
    symbol = 'circle'
    if stage["type"] == "decision":
        symbol = 'diamond'
    elif stage["type"] == "start":
        symbol = 'circle'
    elif stage["type"] == "end":
        symbol = 'circle'
    
    fig.add_trace(go.Scatter(
        x=[stage["x"]],
        y=[stage["y"]],
        mode='markers+text',
        marker=dict(
            size=30,
            color=stage["color"],
            line=dict(width=3, color='white'),
            symbol=symbol
        ),
        text=stage["name"],
        textposition="bottom center",
        textfont=dict(size=11, color='black', family="Arial Black"),
        showlegend=False
    ))

# Add tool labels with better positioning and larger fonts
tools_data = [
    {"stage": 1, "tools": "Git, GitHub", "offset": 1.2},
    {"stage": 2, "tools": "Jenkins", "offset": 1.2},
    {"stage": 3, "tools": "Git Clone", "offset": 1.2},
    {"stage": 4, "tools": "pip, npm", "offset": 1.2},
    {"stage": 5, "tools": "pytest", "offset": 1.2},
    {"stage": 6, "tools": "SonarQube", "offset": 1.2},
    {"stage": 7, "tools": "Trivy", "offset": 1.2},
    {"stage": 8, "tools": "Docker", "offset": 1.2},
    {"stage": 9, "tools": "ECR, Hub", "offset": 1.2},
    {"stage": 10, "tools": "Kubernetes", "offset": 1.2},
    {"stage": 11, "tools": "Postman", "offset": 1.2},
    {"stage": 12, "tools": "Manual", "offset": 1.2},
    {"stage": 13, "tools": "Helm, K8s", "offset": 1.2},
    {"stage": 14, "tools": "Probes", "offset": 1.2},
    {"stage": 15, "tools": "Prometheus", "offset": 1.2},
    {"stage": 16, "tools": "kubectl", "offset": 1.2},
    {"stage": 17, "tools": "Slack", "offset": 1.2}
]

for tool in tools_data:
    stage = stages[tool["stage"]-1]
    fig.add_annotation(
        x=stage["x"],
        y=stage["y"] + tool["offset"],
        text=tool["tools"],
        showarrow=False,
        font=dict(size=10, color='#333', family="Arial"),
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="#999",
        borderwidth=1,
        borderpad=3
    )

# Add prominent legend
legend_y = 11
fig.add_trace(go.Scatter(
    x=[3, 12, 21, 30, 39],
    y=[legend_y, legend_y, legend_y, legend_y, legend_y],
    mode='markers+text',
    marker=dict(size=[20, 20, 20, 20, 20], 
                color=['#4CAF50', '#F44336', '#FFC107', '#2196F3', '#00BCD4']),
    text=['Success', 'Failure', 'Decision', 'Automation', 'Monitor'],
    textposition="top center",
    textfont=dict(size=12, color='black', family="Arial Bold"),
    showlegend=False
))

# Add section dividers
fig.add_annotation(x=7.5, y=10.5, text="CI STAGES", showarrow=False, 
                  font=dict(size=14, color='#2196F3', family="Arial Bold"))
fig.add_annotation(x=30, y=10.5, text="CD STAGES", showarrow=False,
                  font=dict(size=14, color='#009688', family="Arial Bold"))
fig.add_annotation(x=40.5, y=10.5, text="OPS", showarrow=False,
                  font=dict(size=14, color='#00BCD4', family="Arial Bold"))

# Update layout with better spacing
fig.update_layout(
    title=dict(
        text="Complete CI/CD Pipeline",
        font=dict(size=20, color='#333', family="Arial Bold"),
        x=0.5
    ),
    xaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        range=[-2, 45]
    ),
    yaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        range=[1, 12]
    ),
    plot_bgcolor='#f8f9fa',
    paper_bgcolor='white',
    font=dict(family="Arial, sans-serif"),
    showlegend=False
)

# Save the chart
fig.write_image("cicd_pipeline.png")
fig.write_image("cicd_pipeline.svg", format="svg")

print("Enhanced CI/CD Pipeline flowchart created with improved layout and visibility")