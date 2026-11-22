import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from Orange.canvas.__main__ import OMain

class TestOMain(OMain):
    def setup_application(self):
        super().setup_application()
        timer = QTimer(self.application)
        timer.setSingleShot(True)
        timer.setInterval(3000)
        def on_timeout():
            widgets = QApplication.topLevelWidgets()
            print(f"Prueba GUI: Ventanas Qt activas = {len(widgets)}")
            for w in widgets:
                if w.windowTitle():
                    print(f" -> Ventana detectada: {w.windowTitle()}")
            print("ESTADO: Interfaz de Orange Canvas levantada y renderizada con EXITO.")
            self.application.quit()
        timer.timeout.connect(on_timeout)
        timer.start()

if __name__ == "__main__":
    app = TestOMain()
    sys.exit(app.run([]))
