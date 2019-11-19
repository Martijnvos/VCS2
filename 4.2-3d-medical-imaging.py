import vtk
from vtk.util.colors import tan

## Load in skull model
reader = vtk.vtkVolume16Reader()
reader.SetDataDimensions(64,64)
reader.SetImageRange(1,93)
reader.SetDataByteOrderToLittleEndian()
reader.SetFilePrefix("./assets/headsq/quarter")
reader.SetDataSpacing(3.2,3.2,1.5)

## Load in skin model
skinFilePath = r"./assets/skin.vtk"
skinReader = vtk.vtkPolyDataReader()
skinReader.SetFileName(skinFilePath)
skinReader.Update()

## Apply contourfilter to skull model
contourFilter = vtk.vtkContourFilter()
contourFilter.SetInputConnection(reader.GetOutputPort())
### Setting this to 500, 1150 creates a strange ring around most of the skeleton
contourFilter.SetValue(0, 1150)

## Use the information from the contourfilter for the skull mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(contourFilter.GetOutputPort())
mapper.ScalarVisibilityOff()

## Add skin model to mapper
skinMapper = vtk.vtkDataSetMapper()
skinMapper.SetInputConnection(skinReader.GetOutputPort())

# Create actors
actor = vtk.vtkActor()
actor.SetMapper(mapper)

## Create skin actor with changed diffuse color, opacity and specular value
## Also make sure the skin is positioned correctly
skinActor = vtk.vtkActor()
skinActor.SetMapper(skinMapper)
skinActor.RotateX(90)
skinActor.SetPosition(100, 100, 0)
skinActor.GetProperty().SetDiffuseColor(tan)
skinActor.GetProperty().SetOpacity(0.6)
skinActor.GetProperty().SetSpecular(0.4)

# Create a rendering window and renderer

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()

renderWindow.AddRenderer(renderer)

# Create a renderwindowinteractor

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWindow)

# Assign actors to the renderer
renderer.AddActor(actor)
renderer.AddActor(skinActor)

# Enable user interface interactor
interactor.Initialize()
renderWindow.Render()
interactor.Start()