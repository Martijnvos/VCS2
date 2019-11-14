import vtk
from vtk.util.colors import grey

# Initializations
renderWindow = vtk.vtkRenderWindow()
renderer = vtk.vtkRenderer()
# The interactor is necessary for the screen to stay open when running the file
interactor = vtk.vtkRenderWindowInteractor()

coneMapper = vtk.vtkPolyDataMapper()
coneActor = vtk.vtkActor()

# Configuration
renderWindow.AddRenderer(renderer)
interactor.SetRenderWindow(renderWindow)

renderWindow.SetSize(800,800)
renderer.SetBackground(grey)

# Actors
cone = vtk.vtkConeSource()
cone.SetHeight(3.0)
cone.SetRadius(1.0)
cone.SetResolution(20)

coneMapper.SetInputConnection(cone.GetOutputPort())

coneActor.GetProperty().SetColor(1, 0, 0)
coneActor.SetMapper(coneMapper)

renderer.AddActor(coneActor)

# Initialization
interactor.Initialize()
renderWindow.Render()
interactor.Start()