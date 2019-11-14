from vtk import *
from vtk.util.colors import yellow

# Initializations
renderWindow = vtkRenderWindow()
renderer = vtkRenderer()
# The interactor is necessary for the screen to stay open when running the file
interactor = vtkRenderWindowInteractor()

coneMapper = vtkPolyDataMapper()
coneActor = vtkActor()

cylinderMapper = vtkPolyDataMapper()
cylinderActor = vtkActor()

# Configuration
renderWindow.AddRenderer(renderer)
interactor.SetRenderWindow(renderWindow)

renderWindow.SetSize(800,800)

# Actors
## Cylinder
cylinder = vtkCylinderSource()
cylinder.SetHeight(4.0)
cylinder.SetRadius(4.0)

cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

cylinderActor.GetProperty().SetColor(0, 1, 0)
cylinderActor.SetMapper(cylinderMapper)

renderer.AddActor(cylinderActor)

## Cone
cone = vtkConeSource()
cone.SetHeight(12.0)
cone.SetRadius(3.0)
cone.SetResolution(120)

transform = vtkTransform()
transform.Translate(5.0, 0.0, 0.0)

coneMapper.SetInputConnection(cone.GetOutputPort())
coneActor.SetUserTransform(transform)
coneActor.GetProperty().SetColor(1, 0, 0)
coneActor.GetProperty().SetDiffuse(0.7)
coneActor.GetProperty().SetSpecular(0.4)
coneActor.GetProperty().SetSpecularPower(20)
coneActor.SetMapper(coneMapper)

renderer.AddActor(coneActor)

## Camera
## Remark: I could only find GetViewPlaneNormal (https://vtk.org/doc/nightly/html/classvtkCamera.html),
## not ComputerViewPlaneNormal as described in the document
camera = vtkCamera()
### Center camera on x position between cone and cylinder (5/2)
camera.SetPosition(2.5, 0, 0)
### Change the focal point of the camera in world coordinates
camera.SetFocalPoint(0, 5, 0)
### Set near and far clipping ranges, which default to .1, 1000
camera.SetClippingRange(1, 200)
### Default is 0, 1, 0 because Y is up
camera.SetViewUp(0, 0 , 1)
camera.Zoom(.2)
### Divide the camera's distance from the focal point by the given dolly value.
### Use a value greater than one to dolly-in toward the focal point, and use a value less than one to dolly-out away from the focal point.
camera.Dolly(0.2)

renderer.SetActiveCamera(camera)

## Light

light = vtkLight()
light.SetColor(yellow)
### Change the light's position relative to the coordinate space
light.SetPosition(3, 0, 0)
### Sets the point at which the light is shining, in this case the root of the coordinate space
light.SetFocalPoint(0, 0, 0)
### Useful for shining a light on a particular surface, like a flashlight, instead of the whole plane
# light.PositionalOn()

renderer.AddLight(light)

# Initialization
interactor.Initialize()
renderWindow.Render()
interactor.Start()