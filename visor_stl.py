from Tkinter import Tk
from tkFileDialog import askopenfilename
import vtk
import ctypes

while(True):
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    if filename.lower().endswith('.stl'):
        break
    else:
        if not filename:
            exit(1)
        else:
            ctypes.windll.user32.MessageBoxW(0, u"La extension ha de ser STL" , u"Error de extension" , 0)

reader = vtk.vtkSTLReader()
reader.SetFileName(filename)
mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(reader.GetOutput())
else:
    mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# Create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Assign actor to the renderer
ren.AddActor(actor)

# Enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()
