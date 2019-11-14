import vtk
from vtk.util.colors import grey

# Initializations
renderWindow = vtk.vtkRenderWindow()
renderer = vtk.vtkRenderer()
# The interactor is necessary for the screen to stay open when running the file
interactor = vtk.vtkRenderWindowInteractor()

# Configuration
renderWindow.AddRenderer(renderer)
interactor.SetRenderWindow(renderWindow)

renderWindow.SetSize(500,500)
renderer.SetBackground(grey)

# Initialization
interactor.Initialize()
renderWindow.Render()
interactor.Start()
