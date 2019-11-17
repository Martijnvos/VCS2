import vtk

quadric = vtk.vtkQuadric()
quadric.SetCoefficients(.5, 1, .2, 0, .1, 0, 0 , .2, 0, 0)

sample = vtk.vtkSampleFunction()
sample.SetSampleDimensions(30, 30, 30)
sample.SetImplicitFunction(quadric)
sample.ComputeNormalsOff()

extract = vtk.vtkExtractVOI()
extract.SetInputConnection(sample.GetOutputPort())
extract.SetVOI(0, 29, 0, 29, 15, 15)
extract.SetSampleRate(1, 2, 3)

contours = vtk.vtkContourFilter()
contours.SetInputConnection(extract.GetOutputPort())
contours.GenerateValues(13, 0.0, 1.2)

contMapper = vtk.vtkPolyDataMapper()
contMapper.SetInputConnection(contours.GetOutputPort())
contMapper.SetScalarRange(0.0, 1.2)

actor = vtk.vtkActor()
actor.SetMapper(contMapper)

# Create a rendering window and renderer

renderer = vtk.vtkRenderer()
renderer.SetBackground(1, 1, 1)
renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(500, 500)

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