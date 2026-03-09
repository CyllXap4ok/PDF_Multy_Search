import enum
import os
import platform
import subprocess
import time

import pyautogui
import pyperclip

from document_service.document import Document
from document_service.open_service.open_strategy.document_opening_strategy import DocumentHighlightedOpenStrategy


class PdfViewer(enum.Enum):
    MS_EDGE = [
        os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe")
    ]
    ADOBE_ACROBAT = [
        os.path.expandvars(r"%ProgramFiles%\Adobe\Acrobat DC\Acrobat\Acrobat.exe"),
        os.path.expandvars(r"%ProgramFiles%\Adobe\Acrobat 2020\Acrobat\Acrobat.exe"),
        os.path.expandvars(r"%ProgramFiles%\Adobe\Acrobat 2017\Acrobat\Acrobat.exe"),
        os.path.expandvars(r"%ProgramFiles%\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe")
    ]


class PdfHighlightedOpenStrategy(DocumentHighlightedOpenStrategy):

    def open_document(self, doc: Document):
        system = platform.system()
        path = doc.file_path

        match system:
            case "Windows":
                self._open_windows(path)
            case "Linux":
                pass
            case "Darwin":
                pass

    def _open_windows(self, doc_path: str):
        doc_path = os.path.normpath(doc_path)

        for viewer in PdfViewer:
            for path in viewer.value:
                if os.path.exists(path):
                    if viewer == PdfViewer.MS_EDGE:
                        self._open_with_ms_edge(path, doc_path)
                    elif viewer == PdfViewer.ADOBE_ACROBAT:
                        self._open_with_acrobat(path, doc_path)

                    break
            else:
                continue
            break

    def _open_with_acrobat(self, acrobat_path: str, document_path: str):
        try:
            command = f'"{acrobat_path}" /A "page={self.page}" "{document_path}"'
            subprocess.Popen(command)
            time.sleep(2.5)
            self._simulate_keyboard_input()
            time.sleep(0.2)
            pyautogui.hotkey('enter')

        except subprocess.CalledProcessError as e:
            print(f"Ошибка при открытии документа: {e}")

    def _open_with_ms_edge(self, edge_path: str, document_path: str):
        try:
            file_url = f"file://{document_path}"
            edge_url = f"{file_url}#page={self.page}"
            subprocess.Popen([edge_path, edge_url])
            time.sleep(2.5)
            self._simulate_keyboard_input()

        except subprocess.CalledProcessError as e:
            print(f"Ошибка при запуске Edge: {e}")

    def _simulate_keyboard_input(self):
        old_clipboard = pyperclip.paste()
        pyperclip.copy(self.query)

        with pyautogui.hold('ctrl'):
            pyautogui.press('f')
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'v')

        pyperclip.copy(old_clipboard)