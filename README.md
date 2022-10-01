# pyrender-test
Test code of pyrender

## How to use
 - Install pyrender package to the subdirectory.
     - You don't need to care about the Warning message.
  ```
  pip install pyrender -t packages
  ```
 - Run command with model path.
  ```
  python test-model.py {model path}
  ```
## How to check the package size
 - You can check the package size by running the below command with Powershell.
```
$fso = new-object -com Scripting.FileSystemObject
gci -Directory `
   | select @{l='Size'; e={$fso.GetFolder($_.FullName).Size}},FullName `
   | sort Size -Descending `
   | ft @{l='Size [MB]'; e={'{0:N2}    ' -f ($_.Size / 1MB)}},FullName
```
 - Currently, the size of pyrender is 229.56MByte.
 
|Size [MB]|Name|
|----|---|
|121.95     |scipy|
|58.35      |numpy|
|9.83       |networkx|
|8.51       |PIL|
|7.90       |OpenGL|
|7.73       |pyglet|
|5.17       |imageio|
|2.85       |trimesh|
|2.55       |pyrender|
|1.80       |freetype|
|1.64       |share|
|0.31       |bin|
|0.29       |PyOpenGL-3.1.0-py3.10.egg-info|
|0.23       |scipy-1.9.1.dist-info|
|0.15       |numpy-1.23.3.dist-info|
|0.11       |networkx-2.8.6.dist-info|
|0.04       |pyglet-1.5.27.dist-info|
|0.03       |trimesh-3.15.2.dist-info|
|0.03       |__pycache__|
|0.02       |Pillow-9.2.0.dist-info|
|0.01       |imageio-2.22.0.dist-info|
|0.01       |freetype_py-2.3.0.dist-info|
|0.01       |pyrender-0.1.45.dist-info|
|0.00       |six-1.16.0.dist-info|