import vtk

objectPath = r"./assets/density.vtk"

reader = vtk.vtkStructuredGridReader()
reader.SetFileName(objectPath)
reader.Update()

lookupTable = vtk.vtkLookupTable()
lookupTable.SetNumberOfColors(16)
lookupTable.SetHueRange(0, 1)
## Reverse the hue range
# lookupTable.SetHueRange(1, 0)
# lookupTable.SetSaturationRange(0.0, 1.0)
# lookupTable.SetValueRange(0.0, 1.0)
# lookupTable.SetAlphaRange(0.0, 1.0)
# lookupTable.SetRange(0.0, 255.0)

colorMapper = vtk.vtkDataSetMapper()
colorMapper.SetInputConnection(reader.GetOutputPort())
colorMapper.SetLookupTable(lookupTable)
colorMapper.SetScalarRange(reader.GetOutput().GetScalarRange())

actor = vtk.vtkActor()
actor.SetMapper(colorMapper)

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