import vtk

filePath = r"./assets/density.vtk"

reader = vtk.vtkStructuredGridReader()
reader.SetFileName(filePath)
reader.Update()

contourFilter = vtk.vtkContourFilter()
contourFilter.SetInputConnection(reader.GetOutputPort())
contourFilter.SetValue(0, 0.26)
# contourFilter.SetValue(0, 0.5)

contourMapper = vtk.vtkPolyDataMapper()
contourMapper.SetInputConnection(contourFilter.GetOutputPort())
contourMapper.SetScalarRange(reader.GetOutput().GetScalarRange())

actor = vtk.vtkActor()
actor.SetMapper(contourMapper)

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