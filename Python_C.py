from ctypes import cdll
lib = cdll.LoadLibrary(r"C:\Anderson\Pessoal\01_Doutorado\3_Codigos\Python_C\test.dll")
print lib.plop()
print lib.sum(2)
