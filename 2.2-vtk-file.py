from vtk import vtkStructuredPointsReader
from vtk import *

objectPath = r"./assets/brain.vtk"

reader = vtkStructuredPointsReader()
reader.SetFileName(objectPath)
reader.ReadAllVectorsOn()
reader.ReadAllScalarsOn()
reader.Update()

brainMapper = vtkDataSetMapper()
brainMapper.SetInputConnection(reader.GetOutputPort())

actor = vtkActor()
actor.SetMapper(brainMapper)

# Create a rendering window and renderer

renderer = vtkRenderer()
renderWindow = vtkRenderWindow()

renderWindow.AddRenderer(renderer)

# Create a renderwindowinteractor

interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWindow)

# Assign actor to the renderer
renderer.AddActor(actor)

# Enable user interface interactor
interactor.Initialize()
renderWindow.Render()
interactor.Start()