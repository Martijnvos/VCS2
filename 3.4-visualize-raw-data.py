import vtk

objectPath = r"./assets/visualize_raw_data.vtk"

reader = vtk.vtkUnstructuredGridReader()
reader.SetFileName(objectPath)
reader.Update()

## Configure the arrow that is being shown
arrow = vtk.vtkArrowSource()
arrow.SetTipResolution(6)
arrow.SetTipRadius(0.1)
arrow.SetTipLength(0.35)
arrow.SetShaftResolution(6)
arrow.SetShaftRadius(0.03)

## Set up the glyph
glyph = vtk.vtkGlyph3D()
glyph.SetInputConnection(reader.GetOutputPort())
glyph.SetSourceConnection(arrow.GetOutputPort())
## Scale the glyph to reasonable proportions
glyph.SetScaleFactor(0.25)

dataMapper = vtk.vtkDataSetMapper()
dataMapper.SetInputConnection(glyph.GetOutputPort())
dataMapper.SetScalarRange(reader.GetOutput().GetScalarRange())

actor = vtk.vtkActor()
actor.SetMapper(dataMapper)

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