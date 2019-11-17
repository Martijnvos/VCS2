## Take note:
## Points in a .vtk file are defined from top to bottom and from left to right
## Same goes for the color scalars

from vtk import *

objectPath = r"./assets/own.vtk"

reader = vtkUnstructuredGridReader()
reader.SetFileName(objectPath)
reader.Update()

vtkMapper = vtkDataSetMapper()
vtkMapper.SetInputConnection(reader.GetOutputPort())

actor = vtkActor()
actor.SetMapper(vtkMapper)

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