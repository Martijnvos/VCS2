import vtk

objectPath = r"./assets/density.vtk"

reader = vtk.vtkStructuredGridReader()
reader.SetFileName(objectPath)
reader.Update()

hedgehog = vtk.vtkHedgeHog()
hedgehog.SetInputConnection(reader.GetOutputPort())
## Limit magnitude scale in order to show nicely instead of stick out everywhere
hedgehog.SetScaleFactor(0.001)

lookupTable = vtk.vtkLookupTable()
lookupTable.SetNumberOfColors(16)

hedgehogMapper = vtk.vtkPolyDataMapper()
hedgehogMapper.SetInputConnection(hedgehog.GetOutputPort())
hedgehogMapper.SetLookupTable(lookupTable)
hedgehogMapper.SetScalarRange(reader.GetOutput().GetScalarRange())

actor = vtk.vtkActor()
actor.SetMapper(hedgehogMapper)

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