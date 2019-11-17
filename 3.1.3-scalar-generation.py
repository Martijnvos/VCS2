import vtk

objectPath = r"./assets/honolulu.vtk"

reader = vtk.vtkPolyDataReader()
reader.SetFileName(objectPath)
reader.Update()

## Get bounds from the reader and apply the elevation filter accordingly
## bounds is of the form [xmin,xmax, ymin,ymax, zmin,zmax]
bounds = reader.GetOutput().GetBounds()
elevationFilter = vtk.vtkElevationFilter()
elevationFilter.SetInputConnection(reader.GetOutputPort())
elevationFilter.SetLowPoint(0, 0, bounds[4])
elevationFilter.SetHighPoint(0, 0, bounds[5])

elevationMapper = vtk.vtkDataSetMapper()
elevationMapper.SetInputConnection(elevationFilter.GetOutputPort())
## Remove coloring from output
elevationMapper.ScalarVisibilityOff()

actor = vtk.vtkActor()
actor.SetMapper(elevationMapper)

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