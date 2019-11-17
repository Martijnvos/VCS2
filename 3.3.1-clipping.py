import vtk

objectPath = r"./assets/density.vtk"

reader = vtk.vtkStructuredGridReader()
reader.SetFileName(objectPath)
reader.Update()

# plane = vtk.vtkPlane()
# plane.SetOrigin(reader.GetOutput().GetCenter())
# plane.SetNormal(0.5, 0.5, 0.5)

# planeClip = vtk.vtkClipDataSet()
# planeClip.SetInputConnection(reader.GetOutputPort())
# planeClip.SetClipFunction(plane)

sphere = vtk.vtkSphere()
sphere.SetCenter(0, 0, 0)
sphere.SetRadius(30)

sphereClip = vtk.vtkClipDataSet()
sphereClip.SetInputConnection(reader.GetOutputPort())
sphereClip.SetClipFunction(sphere)

clipMapper = vtk.vtkDataSetMapper()
# clipMapper.SetInputConnection(planeClip.GetOutputPort())
clipMapper.SetInputConnection(sphereClip.GetOutputPort())
clipMapper.SetScalarRange(reader.GetOutput().GetScalarRange())

actor = vtk.vtkActor()
actor.SetMapper(clipMapper)

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