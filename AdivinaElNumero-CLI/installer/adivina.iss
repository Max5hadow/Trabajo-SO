#define MyAppName "AdivinaElNumero-CLI"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "TrabajoSO"
#define MyAppExeName "adivina.exe"

[Setup]
AppId={{E8D3D0E0-8F88-41C1-A3C0-0987654321CD}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputBaseFilename=AdivinaElNumero-Setup
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64

ChangesEnvironment=yes

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "addtopath"; Description: "Agregar AdivinaElNumero-CLI al PATH del sistema"; Flags: checkedonce

[Files]
Source: "..\dist\adivina.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "mi_algoritmo_version.bat"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\AdivinaElNumero-CLI"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\AdivinaElNumero-CLI"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\mi_algoritmo_version.bat"; Description: "Verificar instalación (mostrar versión)"; Flags: nowait postinstall runhidden

[UninstallDelete]
Type: files; Name: "{app}\mi_algoritmo_version.bat"

[Registry]
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; \
  ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Check: AddPath

[Code]
function AddPath(): Boolean;
begin
  Result := WizardIsTaskSelected('addtopath');
end;
