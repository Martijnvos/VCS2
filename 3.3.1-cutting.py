import vtk

objectPath = r"./assets/density.vtk"

reader = vtk.vtkStructuredGridReader()
reader.SetFileName(objectPath)
reader.Update()

plane = vtk.vtkPlane()
plane.SetOrigin(reader.GetOutput().GetCenter())
plane.SetNormal(0.5, 0.5, 0.5)

planeCut = vtk.vtkCutter()
planeCut.SetInputConnection(reader.GetOutputPort())
planeCut.SetCutFunction(plane)

cutMapper = vtk.vtkPolyDataMapper()
cutMapper.SetInputConnection(planeCut.GetOutputPort())
cutMapper.SetScalarRange(reader.GetOutput().GetScalarRange())

actor = vtk.vtkActor()
actor.SetMapper(cutMapper)

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