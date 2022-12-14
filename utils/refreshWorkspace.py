#!/usr/bin/env /usr/bin/python


import ujson as UJ
import sys as SYS
from CF.SUBM_D import _00_OS as CF_OS


CBRCE = "}"
CBRKT = "]"
DBLQT = '"'
NEWLINE = "\n"
OBRCE = "{"
OBRKT = "["


if (
    (len(SYS.argv) != 4)
):
  print(f"""
Usage:
  {SYS.argv[0]} <extension path> <workspace path> <file path>
I got {SYS.argv}
""")
  SYS.exit(1)


locals().update(CF_OS.V.ALL_THE_KEYS)


class refreshThem:

  def __init__(self):
    self.EXTENSION_LIST = []
    self.EXTENSION_PATH = SYS.argv[1]
    self.FILE_LIST = []
    self.FILE_PATH = SYS.argv[3]
    self.LOCAL_DICT = {}
    self.WORKSPACE_PATH = SYS.argv[2]
    self.WORKSPACE_NAME = self.WORKSPACE_PATH[self.WORKSPACE_PATH.rfind("/"):]

    try:
      with open(f"""{self.EXTENSION_PATH}/.vscode/kenningsSettings.json""", "tr") as _FDIn_:
        self.KENNINGS_EXTENSION_SETTINGS = UJ.load(_FDIn_)
    except FileNotFoundError:
      self.KENNINGS_EXTENSION_SETTINGS = {}
    try:
      if (
          (self,WORKSPACE_NAME == "kenningsVSC")
      ):
        _workspaceSettingsName_ = "kenningSettingsDev.json"
      else:
        _workspaceSettingsName_ = "kenningSettings.json"
      with open(f"""{self.WORKSPACE_PATH}/.vscode/{_workspaceSettingsName_}""", "tr") as _FDIn_:
        self.KENNINGS_WORKSPACE_SETTINGS = UJ.load(_FDIn_)
    except FileNotFoundError:
      self.KENNINGS_WORKSPACE_SETTINGS = {}
    self.KENNINGS_COMBINED_SETTINGS = {}
    try:
      _listToRtn_ = self.KENNINGS_EXTENSION_SETTINGS["ignoreList"]
    except KeyError:
      _listToRtn_ = []
    try:
      _listToRtn_.append(self.KENNINGS_WORKSPACE_SETTINGS["ignoreList"])
    except  KeyError:
      pass
    self.IGNORE_LIST = set(_listToRtn_)

  def doExtensionList(self):
    _listToRtn_ = CF_OS.filteredLpathGlobListPieces(
        rootDir_=self.FILE_PATH,
        ignoreList_=self.KENNINGS_SETTINGS["ignoreList"]
    )
    self.EXTENSION_LIST = []
    for _thisItem_ in _listToRtn_:
      if (
          (_thisItem_[K_EXTENSION] != "")
      ):
        self.EXTENSION_LIST.append(_thisItem_[K_EXTENSION])
    self.EXTENSION_LIST = sorted(set(self.EXTENSION_LIST))

  def doExtensionPath(self):
    pass

  def doWorkspacePath(self):
    pass

  def doFilePath(self):
    pass

  def writeQuickFiles(self):
    pass


def __main__():
  refreshClass = refreshThem()
  # refreshClass.doExtensionList()
  # refreshClass.doExtensionPath()
  # refreshClass.doWorkspacePath()
  # refreshClass.doFilePath()
  # refreshClass.writeQuickFiles()

  # _result_ = CF_OS.globList(
  #     source_="**",
  #     root_dir_="/rcr/0-sourceCode/0-development/0-ide/0-vscode/0-extensions/kenningsVSC",
  #     recursive_=True,
  # )
  # with open("/rcr/0-sourceCode/0-development/0-ide/0-vscode/0-extensions/kenningsVSC/.vscode/kenningsSettings.json", "tr") as _FDIn_:
  #  _kenningsSettings_ = UJ.load(_FDIn_)
  # _listToRtn_ = CF_OS.filteredLpathGlobListPieces(
  #    rootDir_="/rcr/0-sourceCode/0-development/0-ide/0-vscode/0-extensions/kenningsVSC",
  #    ignoreList_=_kenningsSettings_["ignoreList"]
  # )
  # with open("/rcr/0-sourceCode/0-development/0-ide/0-vscode/0-extensions/kenningsVSC/.junk/File_003.json", "tw") as _FDOut_:
  #   UJ.dump(_listToRtn_, _FDOut_, indent=2, escape_forward_slashes=False)
  #   _FDOut_.flush()
  #   _FDOut_.close()

__main__()



#
