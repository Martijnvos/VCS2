import vtk

texturePath = r"./assets/land.bmp"

bmpReader = vtk.vtkBMPReader()
bmpReader.SetFileName(texturePath)
texture = vtk.vtkTexture()
texture.SetInputConnection(bmpReader.GetOutputPort())
texture.InterpolateOn()

# Create a plane source and actor. The vtkPlanesSource generates
# texture coordinates.
plane = vtk.vtkPlaneSource()
planeMapper = vtk.vtkPolyDataMapper()
planeMapper.SetInputConnection(plane.GetOutputPort())
planeActor = vtk.vtkActor()
planeActor.SetMapper(planeMapper)
planeActor.SetTexture(texture)

# Create the RenderWindow, Renderer and both Actors
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Add the actors to the renderer, set the background and size
ren.AddActor(planeActor)
renWin.SetSize(500, 500)

iren.Initialize()
renWin.Render()
iren.Start()