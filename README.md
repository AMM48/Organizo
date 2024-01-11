# Organizo
Organizo is an automated file organization tool. It monitors the Downloads directory and automatically moves files to their designated folders based on their extensions.
The script handles various file types, supports notifications, and ensures smooth operation even with temporary or in-use files.
It’s a simple yet efficient solution for keeping your downloads folder clutter-free and well-organized.

## Supported Extensions & Folders
<table>
  <tr>
    <th>Extensions</th>
    <th>Folder</th>
  </tr>
  <tr>
    <td>.pdf</td>
    <td>PDFs</td>
  </tr>
  <tr>
    <td>.jpg</td>
    <td rowspan="5">Images</td>
  </tr>
  <tr>
    <td>.jpeg</td>
  </tr>
  <tr>
    <td>.png</td>
  </tr>
  <tr>
    <td>.gif</td>
  </tr>
  <tr>
    <td>.svg</td>
  </tr>
  <tr>
    <td>.doc</td>
    <td rowspan="2">Word</td>
  </tr>
  <tr>
    <td>.docx</td>
  </tr>
  <tr>
    <td>.ppt</td>
    <td rowspan="2">PowerPoint</td>
  </tr>
  <tr>
    <td>.pptx</td>
  </tr>
  <tr>
    <td>.xlsx</td>
    <td rowspan="3">Excel</td>
  </tr>
  <tr>
    <td>.xls</td>
  </tr>
  <tr>
    <td>.csv</td>
  </tr>
  <tr>
    <td>.exe</td>
    <td>EXEs</td>
  </tr>
  <tr>
    <td>.txt</td>
    <td rowspan="3">Texts</td>
  </tr>
  <tr>
    <td>.log</td>
  </tr>
  <tr>
    <td>.md</td>
  </tr>
  <tr>
    <td>.mp3</td>
    <td rowspan="2">Audio</td>
  </tr>
  <tr>
    <td>.wav</td>
  </tr>
  <tr>
    <td>.mp4</td>
    <td>Videos</td>
  </tr>
  <tr>
    <td>.msi</td>
    <td>MSIs</td>
  </tr>
  <tr>
    <td>.iso</td>
    <td>ISOs</td>
  </tr>
  <tr>
    <td>.zip</td>
    <td rowspan="6">ZIPs</td>
  </tr>
  <tr>
    <td>.rar</td>
  </tr>
  <tr>
    <td>.tar</td>
  </tr>
  <tr>
    <td>.tgz</td>
  </tr>
  <tr>
    <td>.gz</td>
  </tr>
  <tr>
    <td>.7z</td>
  </tr>
  <tr>
    <td>Other Extensions</td>
    <td>Trash</td>
  </tr>
</table>

## Usage
Clone the script:
```PS1
  
git clone https://github.com/AMM48/Organizo.git
  
```
Execute the script as a background job:
```PS1
  
Start-Job -ScriptBlock { python.exe "<Path-To-Script>" }
  
```
## Notes
Please be aware that this script does not automatically create the necessary folders, and if a required folder is missing, the script may not execute successfully. Additionally, I plan to expand the range of supported file extensions in the future, which may lead to changes in the folder structure. Furthermore, upon execution, the script will immediately organize and sort the existing files in your downloads folder.
