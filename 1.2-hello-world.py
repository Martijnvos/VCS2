from vtk import *

# Initializations
renderWindow = vtkRenderWindow()
renderer = vtkRenderer()
# The interactor is necessary for the screen to stay open when running the file
interactor = vtkRenderWindowInteractor()

text = vtkTextSource()
textMapper = vtkPolyDataMapper()
textActor = vtkActor()

# Configuration
renderWindow.AddRenderer(renderer)
interactor.SetRenderWindow(renderWindow)

renderWindow.SetSize(500,500)
renderer.SetBackground(1,1,1)

# Actors

text.SetText("Hello World")
text.SetForegroundColor(1, 0, 0)

textMapper.SetInputConnection(text.GetOutputPort())
textActor.SetMapper(textMapper)

renderer.AddActor(textActor)

# Initialization
interactor.Initialize()
renderWindow.Render()
interactor.Start()


