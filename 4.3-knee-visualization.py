import vtk
from vtk.util.colors import tan

## Load in knee model
kneeFile = r"./assets/vw_knee.slc"
kneeReader = vtk.vtkSLCReader()
kneeReader.SetFileName(kneeFile)

## Apply contourfilter to knee skin model
kneeSkinContourFilter = vtk.vtkContourFilter()
kneeSkinContourFilter.SetInputConnection(kneeReader.GetOutputPort())
kneeSkinContourFilter.SetValue(0, 50)

## Clip the knee skin
sphere = vtk.vtkSphere()
sphere.SetCenter(0, 0, 50)
sphere.SetRadius(100)

sphereClip = vtk.vtkClipPolyData()
sphereClip.SetInputConnection(kneeSkinContourFilter.GetOutputPort())
sphereClip.GenerateClippedOutputOn()
sphereClip.GenerateClipScalarsOn()
sphereClip.SetClipFunction(sphere)

## Apply contour filter to knee itself
kneeContourFilter = vtk.vtkContourFilter()
kneeContourFilter.SetInputConnection(kneeReader.GetOutputPort())
kneeContourFilter.SetValue(0, 80)

## Smoothen everything up by sampling less
kneeExtractVOI = vtk.vtkExtractVOI()
kneeExtractVOI.SetInputConnection(kneeReader.GetOutputPort())
kneeExtractVOI.SetSampleRate(2, 2, 2)

## Use the information from the clipped contour filter for the knee skin mapper
kneeSkinmapper = vtk.vtkPolyDataMapper()
kneeSkinmapper.SetInputConnection(sphereClip.GetOutputPort())
kneeSkinmapper.ScalarVisibilityOff()

## Use the information from the knee contour filter for the knee mapper
kneeMapper = vtk.vtkPolyDataMapper()
kneeMapper.SetInputConnection(kneeContourFilter.GetOutputPort())
kneeMapper.ScalarVisibilityOff()

# Create actors
kneeSkinActor = vtk.vtkActor()
kneeSkinActor.SetMapper(kneeSkinmapper)
## Change knee skin properties such as color and opacity
kneeSkinActor.GetProperty().SetDiffuseColor(tan)
kneeSkinActor.GetProperty().SetOpacity(0.6)
kneeSkinActor.GetProperty().SetSpecular(0.4)

kneeActor = vtk.vtkActor()
kneeActor.SetMapper(kneeMapper)

# Create a rendering window and renderer

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()

renderWindow.AddRenderer(renderer)

# Create a renderwindowinteractor

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWindow)

# Assign actors to the renderer
renderer.AddActor(kneeSkinActor)
renderer.AddActor(kneeActor)

# Enable user interface interactor
interactor.Initialize()
renderWindow.Render()
interactor.Start()