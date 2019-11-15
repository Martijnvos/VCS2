import vtk
from vtk.util.colors import ivory

# Initializations
renderWindow = vtk.vtkRenderWindow()
renderer = vtk.vtkRenderer()
# The interactor is necessary for the screen to stay open when running the file
interactor = vtk.vtkRenderWindowInteractor()

kneeReader = vtk.vtkSLCReader()
kneeContourFilter = vtk.vtkContourFilter()
kneeOutlineFilter = vtk.vtkOutlineFilter()
kneeExtractVOI = vtk.vtkExtractVOI()
kneeMapper = vtk.vtkPolyDataMapper()
kneeActor = vtk.vtkActor()

kneeFile = r"./assets/vw_knee.slc"

# Configuration
renderWindow.AddRenderer(renderer)
interactor.SetRenderWindow(renderWindow)
kneeReader.SetFileName(kneeFile)

renderWindow.SetSize(800,800)

## Gets the contours of the knee file and displays it with the given amount of density units on the first layer (index based)
kneeContourFilter.SetInputConnection(kneeReader.GetOutputPort())
kneeContourFilter.SetValue(0, 80)

## Adding the outliner
kneeOutlineFilter.SetInputConnection(kneeReader.GetOutputPort())

## Fix subsample problem for smoothness
kneeExtractVOI.SetInputConnection(kneeReader.GetOutputPort())
kneeExtractVOI.SetSampleRate(2, 2, 2)

## Use the countour filter to display the final image
kneeMapper.SetInputConnection(kneeContourFilter.GetOutputPort())
## Remove the default color table
kneeMapper.SetScalarVisibility(0)

kneeActor.SetMapper(kneeMapper)
kneeActor.GetProperty().SetColor(ivory)
renderer.AddActor(kneeActor)

# Initialization
interactor.Initialize()
renderWindow.Render()
interactor.Start()