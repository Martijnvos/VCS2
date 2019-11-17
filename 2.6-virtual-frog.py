import vtk

def CreateFrogActor(tissue):
    fileName = './assets/frog/{}.vtk'.format(tissue)

    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(fileName)
    reader.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor

def CreateFrogLut():
    colorLut = vtk.vtkLookupTable()
    colorLut.SetNumberOfColors(17)
    colorLut.SetTableRange(0, 16)
    colorLut.Build()
                #  blood   brain  duodenum   eye_retina  eye_white  heart       ileum      kidney  intestine liver      lung        nerve   skeleton   spleen   stomach
    colorList = ["salmon", "red", "orange", "misty_rose", "white", "tomato", "raspberry", "banana", "peru", "pink", "powder_blue", "carrot", "wheat", "violet", "plum"]

    colorLut.SetTableValue(0, 0, 0, 0, 0)
    for i in range(1, 16):
        colorLut.SetTableValue(i, colors.GetColor4d(colorList[i - 1]))

    return colorLut

def CreateTissueMap():
    keys = tissues
    values = [i for i in range(1, 16)]
    return dict(zip(keys, values))

# Main program that's being run after function declarations
tissues = ["blood", "brain", "duodenum", "eye_retina", "eye_white", "heart", "ileum", "kidney", "intestine", 
    "liver", "lung", "nerve", "skeleton", "spleen", "stomach"]
colors = vtk.vtkNamedColors()

tissueMap = CreateTissueMap()
colorLut = CreateFrogLut()

# Setup render window, renderer, and interactor.
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

for tissue in tissues:
    actor = CreateFrogActor(tissue)
    actor.GetProperty().SetDiffuseColor(colorLut.GetTableValue(tissueMap[tissue])[:3])
    actor.GetProperty().SetSpecular(.5)
    actor.GetProperty().SetSpecularPower(10)
    renderer.AddActor(actor)

renderer.GetActiveCamera().SetViewUp(-1, 0, -1)
renderer.GetActiveCamera().SetPosition(0, -1, 0)

renderer.GetActiveCamera().Azimuth(210)
renderer.GetActiveCamera().Elevation(30)
renderer.ResetCamera()
renderer.ResetCameraClippingRange()
renderer.GetActiveCamera().Dolly(1.5)
renderer.SetBackground(colors.GetColor3d("SlateGray"))

renderWindow.SetSize(640, 480)
renderWindow.Render()

renderWindowInteractor.Start()