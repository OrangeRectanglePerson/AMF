# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:\\Users\\Devon\\OneDrive\\OneDrive - NUS High School\\personal stuff\\kode projects\\AMF\\desktop version\\AMFd_v1r2\\AMFd_v1r2.py'],
             pathex=['D:\\Users\\Devon\\OneDrive\\OneDrive - NUS High School\\personal stuff\\kode projects\\AMF\\desktop version\\AMFd_v1r2'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='AMFd_v1r2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
