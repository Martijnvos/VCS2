import vtk

objectPath = r"./assets/density.vtk"

reader = vtk.vtkStructuredGridReader()
reader.SetFileName(objectPath)
reader.Update()

seeds = vtk.vtkPointSource()
seeds.SetRadius(3.0)
seeds.SetCenter(reader.GetOutput().GetCenter())
seeds.SetNumberOfPoints(100)

integrator = vtk.vtkRungeKutta4()

streamer = vtk.vtkStreamTracer()
streamer.SetInputConnection(reader.GetOutputPort())
streamer.SetSourceConnection(seeds.GetOutputPort())
streamer.SetMaximumPropagation(100)
## TIME_UNIT Doesn't exist anymore... see https://vtk.org/doc/nightly/html/classvtkStreamTracer.html#a80f1503728603955364e1618af963ab1
#streamer.SetMaximumPropagationUnit(TIME_UNIT)
## LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2
streamer.SetInitialIntegrationStep(2)
streamer.SetInitialIntegrationStep(0.1)
streamer.SetIntegrationDirectionToBoth()
streamer.SetIntegrator(integrator)

streamlineMapper = vtk.vtkPolyDataMapper()
streamlineMapper.SetInputConnection(streamer.GetOutputPort())
streamlineMapper.SetScalarRange(reader.GetOutput().GetScalarRange())

actor = vtk.vtkActor()
actor.SetMapper(streamlineMapper)

# Create a rendering window and renderer

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()

renderWindow.AddRenderer(renderer)

# Create a renderwindowinteractor

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWindow)

# Assign actor to the renderer
renderer.AddActor(actor)

# Enable user interface interactor
interactor.Initialize()
renderWindow.Render()
interactor.Start()