import vtk

objectPath = r"./assets/torso.vtk"

reader = vtk.vtkStructuredPointsReader()
reader.SetFileName(objectPath)
reader.Update()

raycasting_function = vtk.vtkVolumeRayCastMIPFunction()

volumeMapper = vtk.vtkVolumeRayCastMapper()
volumeMapper.SetVolumeRayCastFunction(raycasting_function)
volumeMapper.SetInputConnection(reader.GetOutputPort())

volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)

# Create a rendering window and renderer

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()

renderWindow.AddRenderer(renderer)

# Create a renderwindowinteractor

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWindow)

# Assign volume to the renderer
renderer.AddVolume(volume)

# Enable user interface interactor
interactor.Initialize()
renderWindow.Render()
interactor.Start()